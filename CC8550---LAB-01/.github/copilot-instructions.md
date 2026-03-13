# AI Coding Agent Instructions for pytest Grading System

## Project Overview
This is a student grading system that validates and analyzes student notes/grades. The core module [src/notas.py](src/notas.py) provides utility functions for grade management, and [tests/test_notas.py](tests/test_notas.py) contains comprehensive pytest test suites with 100% code coverage (25 tests total).

## Architecture & Core Functions

### Grade Validation & Processing Pipeline
- **`validar_nota(nota)`** - Gate function that type-checks and validates grades (0-10 range), returns bool
- **`calcular_media(notas)`** - Filters valid grades via `validar_nota()`, ignores invalid entries, returns mean (0 if empty)
- **`obter_situacao(media)`** - Maps mean to status: ≥7 "Aprovado" (Pass), 5-6.99 "Recuperação" (Remedial), <5 "Reprovado" (Fail)
- **`calcular_estatisticas(notas)`** - Returns dict with {maior, menor, media, quantidade} for valid grades
- **`normalizar_notas(notas, max_valor)`** - Converts grades from 0-max_valor scale to 0-10 scale; returns [] if max_valor ≤ 0

**Key Design Pattern**: Functions accept heterogeneous iterables (lists, tuples with mixed types) and gracefully handle invalid data via `validar_nota()` filtering rather than raising exceptions (except for true type errors in computation).

## Testing Conventions (Important for AI Agents)

### Test Structure - AAA Pattern
Every test follows strict **Arrange-Act-Assert** structure:
```python
def test_xxx():
    # ARRANGE - Set up test data
    # ACT - Execute function
    # ASSERT - Verify results
```

### Test Organization
Tests are organized into **test suites by function** using pytest classes:
- `TestValidarNota` - 7 tests for validation edge cases (0, 10, decimals, invalid types, None)
- `TestCalcularMedia` - 5 tests including empty list, mixed valid/invalid, decimals
- `TestObterSituacao` - 6 tests covering boundary conditions (≥7, 5-6.99, <5)
- `TestCalcularEstatisticas` - 5 tests for statistics with various input states
- `TestNormalizarNotas` - 4 tests for scale conversion and edge cases (zero, empty)
- `TestExcecoesReais` - 9 tests that use `pytest.raises()` to test exception handling

### Exception Testing Pattern
Use `pytest.raises()` context manager to test expected TypeErrors:
```python
def test_normalizar_com_max_string_levanta_erro(self):
    with pytest.raises(TypeError):
        normalizar_notas([50], "100")
```
This captures type errors from invalid operations (e.g., string ≤ int, non-iterable iteration).

## Critical Developer Workflows

### Running Tests
```powershell
# Run all tests with coverage report
pytest --cov=src --cov-report=html

# Run specific test class
pytest tests/test_notas.py::TestValidarNota -v

# Run with verbose output
pytest tests/test_notas.py -v
```

### Code Coverage
Coverage reports are generated in `htmlcov/` directory. The project targets 100% coverage (currently achieved). View report at [htmlcov/index.html](htmlcov/index.html).

## Project-Specific Patterns

### Boundary Testing
The codebase extensively tests **boundary values and transitions**:
- Grade validation: Tests both exact boundaries (0, 10) and invalid edges (10.1, -1)
- Status transitions: Tests exact thresholds (media=7.0, 5.0, 4.9)
- Empty/null cases: All functions handle empty lists and None gracefully

### Type Coercion & Error Handling
- `validar_nota()` attempts `float()` conversion, catching `TypeError` and `ValueError` silently
- Functions that expect iterables (lists) fail with `TypeError` if passed non-iterables (int, None, string)
- Non-numeric strings in lists are treated as invalid grades, not exceptions

### Docstring Standard
All functions use detailed docstrings with Args, Returns sections. Follow this format for new functions.

## Integration Points & Dependencies
- **No external dependencies** beyond pytest for testing
- **Single module architecture**: All functions in `src/notas.py`, imported directly in tests
- **Data flow**: User input → validar_nota() → calcular_media() → obter_situacao() + calcular_estatisticas()

## When Adding Features
1. Add function to [src/notas.py](src/notas.py) with full docstring
2. Create new test class in [tests/test_notas.py](tests/test_notas.py) following TestXxxName pattern
3. Include boundary tests (min/max), empty input, mixed valid/invalid data, and exception cases
4. Use AAA pattern strictly with descriptive docstrings for each test
5. Run `pytest --cov=src --cov-report=html` and ensure 100% coverage maintained

## File References
- Core logic: [src/notas.py](src/notas.py)
- Test suites: [tests/test_notas.py](tests/test_notas.py)
- Documentation: [README.md](README.md) (lab assignment overview with screenshots)
