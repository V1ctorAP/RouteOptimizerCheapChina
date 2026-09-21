import pytest
import re
import subprocess
from pathlib import Path
from typing import List, Tuple

def read_file_content(file_path: Path) -> str:
    """Helper to read file content for static analysis."""
    return file_path.read_text(encoding="utf-8")

def search_all_files(pattern: str, root_dir: Path) -> List[Tuple[Path, str]]:
    """Helper to search for regex in all .ts/.tsx files."""
    matches = []
    for file_path in root_dir.glob("**/*.{ts,tsx}"):
        content = read_file_content(file_path)
        for match in re.finditer(pattern, content):
            matches.append((file_path, match.group()))
    return matches

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(0)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_app_ts_contains_new_brand_colors():
    """Verify App.tsx contains the new brand colors (#800020, #A3324A, #5C0017)."""
    src_dir = Path("RouteOptimizer.Web/src")
    app_ts = src_dir / "App.tsx"
    content = read_file_content(app_ts)

    colors = ["#800020", "#A3324A", "#5C0017"]
    for color in colors:
        assert re.search(rf"\b{color}\b", content), f"App.tsx missing color: {color}"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(0)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
# Duplicate test with same vault_ref - assuming this is intentional for redundancy
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_app_ts_contains_new_brand_colors_static_analysis():
    """Verify App.tsx contains the new brand colors."""
    src_dir = Path("RouteOptimizer.Web/src")
    app_ts = src_dir / "App.tsx"
    content = read_file_content(app_ts)

    colors = ["#800020", "#A3324A", "#5C0017"]
    for color in colors:
        assert re.search(rf"\b{color}\b", content), f"App.tsx missing color: {color}"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(1)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_app_ts_contains_georgia_font():
    """Verify App.tsx includes Georgia font family."""
    src_dir = Path("RouteOptimizer.Web/src")
    app_ts = src_dir / "App.tsx"
    content = read_file_content(app_ts)

    assert "Georgia" in content, "App.tsx missing Georgia font family"
    assert "fontFamily" in content, "App.tsx missing fontFamily configuration"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(2)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_app_ts_excludes_legacy_blue_colors():
    """Verify App.tsx does not contain legacy blue colors."""
    src_dir = Path("RouteOptimizer.Web/src")
    app_ts = src_dir / "App.tsx"
    content = read_file_content(app_ts)

    legacy_colors = ["#1976d2", "#42a5f5", "#1565c0"]
    for color in legacy_colors:
        assert not re.search(rf"\b{color}\b", content), f"App.tsx contains legacy color: {color}"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(4)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_login_page_ts_excludes_legacy_blue_colors():
    """Verify LoginPage.tsx does not contain legacy blue colors."""
    src_dir = Path("RouteOptimizer.Web/src")
    login_tsx = src_dir / "LoginPage.tsx"
    content = read_file_content(login_tsx)

    legacy_colors = ["#1976d2", "#42a5f5", "#1565c0"]
    for color in legacy_colors:
        assert not re.search(rf"\b{color}\b", content), f"LoginPage.tsx contains legacy color: {color}"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(5)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_login_page_ts_contains_new_gradient():
    """Verify LoginPage.tsx contains #800020 and linear-gradient(135deg)."""
    src_dir = Path("RouteOptimizer.Web/src")
    login_tsx = src_dir / "LoginPage.tsx"
    content = read_file_content(login_tsx)

    assert "#800020" in content, "LoginPage.tsx missing #800020"
    assert "linear-gradient(135deg" in content, "LoginPage.tsx missing gradient syntax"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(6)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_navbar_ts_contains_account_balance():
    """Verify Navbar.tsx contains AccountBalance import."""
    src_dir = Path("RouteOptimizer.Web/src")
    navbar_tsx = src_dir / "Navbar.tsx"
    content = read_file_content(navbar_tsx)

    assert "AccountBalance" in content, "Navbar.tsx missing AccountBalance import"
    assert "@mui/icons-material" in content, "Navbar.tsx missing MUI icons import"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(7)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_navbar_ts_contains_component_a():
    """Verify Navbar.tsx contains component='a' (assumed Button prop)."""
    src_dir = Path("RouteOptimizer.Web/src")
    navbar_tsx = src_dir / "Navbar.tsx"
    content = read_file_content(navbar_tsx)

    assert 'component="a"' in content, "Navbar.tsx missing component='a'"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(8)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_navbar_ts_contains_pmb_href():
    """Verify Navbar.tsx contains href='https://pmb.ro'."""
    src_dir = Path("RouteOptimizer.Web/src")
    navbar_tsx = src_dir / "Navbar.tsx"
    content = read_file_content(navbar_tsx)

    assert 'href="https://pmb.ro"' in content, "Navbar.tsx missing PMB href"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(9)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_navbar_ts_contains_target_and_rel():
    """Verify Navbar.tsx contains target='_blank' and rel='noopener noreferrer'."""
    src_dir = Path("RouteOptimizer.Web/src")
    navbar_tsx = src_dir / "Navbar.tsx"
    content = read_file_content(navbar_tsx)

    assert 'target="_blank"' in content, "Navbar.tsx missing target='_blank'"
    assert 'rel="noopener noreferrer"' in content, "Navbar.tsx missing rel='noopener noreferrer'"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(10)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_navbar_ts_contains_inherit_color():
    """Verify Navbar.tsx contains color='inherit'."""
    src_dir = Path("RouteOptimizer.Web/src")
    navbar_tsx = src_dir / "Navbar.tsx"
    content = read_file_content(navbar_tsx)

    assert 'color="inherit"' in content, "Navbar.tsx missing color='inherit'"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(11)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_navbar_ts_contains_accessibility_attributes():
    """Verify Navbar.tsx contains aria-label and title attributes."""
    src_dir = Path("RouteOptimizer.Web/src")
    navbar_tsx = src_dir / "Navbar.tsx"
    content = read_file_content(navbar_tsx)

    assert 'aria-label' in content, "Navbar.tsx missing aria-label"
    assert 'title' in content, "Navbar.tsx missing title"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(12)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-488a7caf")
def test_navbar_ts_excludes_forbidden_props():
    """Verify Navbar.tsx does not contain window.open, variant='contained', or color='secondary'."""
    src_dir = Path("RouteOptimizer.Web/src")
    navbar_tsx = src_dir / "Navbar.tsx"
    content = read_file_content(navbar_tsx)

    forbidden_props = ["window.open", 'variant="contained"', 'color="secondary"']
    for prop in forbidden_props:
        assert not re.search(rf"\b{prop}\b", content), f"Navbar.tsx contains forbidden prop: {prop}"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(13)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_navbar_ts_get_role_color_contains_1976d2_once():
    """Verify Navbar.tsx contains #1976d2 exactly once in getRoleColor."""
    src_dir = Path("RouteOptimizer.Web/src")
    navbar_tsx = src_dir / "Navbar.tsx"
    content = read_file_content(navbar_tsx)

    matches = re.findall(r'#1976d2', content)
    assert len(matches) == 1, f"Navbar.tsx contains #1976d2 {len(matches)} times (expected 1)"

@pytest.mark.happyPath
@pytest.mark.staticAnalysis
@pytest.mark.ac_index(14)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_global_search_for_1976d2():
    """Verify #1976d2 appears only in Navbar.tsx across all .ts/.tsx files."""
    src_dir = Path("RouteOptimizer.Web/src")
    matches = search_all_files(r'#1976d2', src_dir)

    assert len(matches) == 1, f"#1976d2 found in {len(matches)} files (expected 1 in Navbar.tsx)"
    assert matches[0][0].name == "Navbar.tsx", f"#1976d2 found in {matches[0][0].name}, expected Navbar.tsx"

@pytest.mark.happyPath
@pytest.mark.cli
@pytest.mark.e2e
@pytest.mark.ac_index(15)
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-69638bb5")
def test_npm_commands_pass(run_command: object):
    """Verify npm run type-check and npm run lint pass (exit code 0)."""
    # Test npm type-check
    result = subprocess.run(["npm", "run", "type-check"], capture_output=True, text=True)
    assert result.returncode == 0, f"npm run type-check failed: {result.stderr}"

    # Test npm lint
    result = subprocess.run(["npm", "run", "lint"], capture_output=True, text=True)
    assert result.returncode == 0, f"npm run lint failed: {result.stderr}"
