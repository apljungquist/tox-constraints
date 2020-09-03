"""pytest is unhappy if it finds no tests"""
import dev

# Dev package may contain tools that we want to test but not make available to any
# other packages.
def test_print_timing_does_not_raise():
    with dev.print_timing("foo"):
        pass
