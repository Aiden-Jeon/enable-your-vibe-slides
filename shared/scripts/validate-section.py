"""
섹션 구조 검증 스크립트

각 섹션이 올바른 파일 구조를 가지고 있는지 확인합니다.

실행:
  python shared/scripts/validate-section.py                    # 전체 섹션 검증
  python shared/scripts/validate-section.py sections/03-mcp-architecture  # 특정 섹션 검증
"""

import ast
import os
import sys

import yaml


def validate_section(section_path: str) -> dict:
    """섹션 디렉토리를 검증하고 결과를 반환합니다."""
    results = {"passed": [], "failed": [], "warnings": []}
    section_name = os.path.basename(section_path)

    # 1. slides/index.html 확인
    slides_path = os.path.join(section_path, "slides", "index.html")
    if os.path.exists(slides_path):
        results["passed"].append("slides/index.html 존재")
        content = open(slides_path, encoding="utf-8").read()
        if "reveal.js" in content:
            results["passed"].append("reveal.js 참조 확인")
        else:
            results["warnings"].append("reveal.js CDN 참조를 찾을 수 없음")
        if "theme.css" in content:
            results["passed"].append("theme.css 참조 확인")
        else:
            results["warnings"].append("theme.css 참조를 찾을 수 없음")
        if '<aside class="notes">' in content:
            results["passed"].append("스피커 노트 포함")
        else:
            results["warnings"].append("스피커 노트가 없음")
    else:
        results["failed"].append("slides/index.html 없음")

    # 2. section.yaml 확인
    yaml_path = os.path.join(section_path, "section.yaml")
    if os.path.exists(yaml_path):
        results["passed"].append("section.yaml 존재")
        with open(yaml_path, encoding="utf-8") as f:
            try:
                meta = yaml.safe_load(f)
                required_fields = ["number", "title", "duration_minutes", "type"]
                for field in required_fields:
                    if field in meta:
                        results["passed"].append(f"section.yaml: {field} 필드 존재")
                    else:
                        results["failed"].append(f"section.yaml: {field} 필드 누락")

                # code_files 교차 검증
                if "code_files" in meta and meta["code_files"]:
                    for code_file in meta["code_files"]:
                        file_path = os.path.join(section_path, code_file)
                        if os.path.exists(file_path):
                            results["passed"].append(f"코드 파일 존재: {code_file}")
                        else:
                            results["failed"].append(f"코드 파일 없음: {code_file}")
            except yaml.YAMLError as e:
                results["failed"].append(f"section.yaml 파싱 에러: {e}")
    else:
        results["failed"].append("section.yaml 없음")

    # 3. code/ 디렉토리 확인
    code_dir = os.path.join(section_path, "code")
    if os.path.exists(code_dir):
        py_files = [f for f in os.listdir(code_dir) if f.endswith(".py")]
        for py_file in py_files:
            py_path = os.path.join(code_dir, py_file)
            try:
                with open(py_path, encoding="utf-8") as f:
                    ast.parse(f.read())
                results["passed"].append(f"구문 검증 통과: {py_file}")
            except SyntaxError as e:
                results["failed"].append(f"구문 에러: {py_file} - {e}")

        readme_path = os.path.join(code_dir, "README.md")
        if os.path.exists(readme_path):
            results["passed"].append("code/README.md 존재")
        else:
            results["warnings"].append("code/README.md 없음")

    return results


def print_results(section_name: str, results: dict):
    """검증 결과를 출력합니다."""
    print(f"\n{'='*60}")
    print(f"  검증 결과: {section_name}")
    print(f"{'='*60}")

    if results["passed"]:
        print(f"\n  ✅ 통과 ({len(results['passed'])}개)")
        for item in results["passed"]:
            print(f"     • {item}")

    if results["failed"]:
        print(f"\n  ❌ 실패 ({len(results['failed'])}개)")
        for item in results["failed"]:
            print(f"     • {item}")

    if results["warnings"]:
        print(f"\n  ⚠️  경고 ({len(results['warnings'])}개)")
        for item in results["warnings"]:
            print(f"     • {item}")

    total = len(results["passed"]) + len(results["failed"]) + len(results["warnings"])
    print(f"\n  요약: 통과 {len(results['passed'])}/{total}")
    print(f"{'='*60}")

    return len(results["failed"]) == 0


def main():
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    if len(sys.argv) > 1:
        # 특정 섹션 검증
        section_path = sys.argv[1]
        if not os.path.isabs(section_path):
            section_path = os.path.join(project_root, section_path)
        results = validate_section(section_path)
        success = print_results(os.path.basename(section_path), results)
        sys.exit(0 if success else 1)
    else:
        # 전체 섹션 검증
        sections_dir = os.path.join(project_root, "sections")
        all_passed = True
        for section_name in sorted(os.listdir(sections_dir)):
            section_path = os.path.join(sections_dir, section_name)
            if os.path.isdir(section_path):
                results = validate_section(section_path)
                if not print_results(section_name, results):
                    all_passed = False

        print(f"\n{'='*60}")
        if all_passed:
            print("  🎉 모든 섹션 검증 통과!")
        else:
            print("  ⚠️  일부 섹션에서 실패 항목이 있습니다.")
        print(f"{'='*60}\n")
        sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
