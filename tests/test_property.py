import isa.isa as isa

from hypothesis import given, strategies, settings

class TestProperty:

    @given(
            strategies.lists(
                strategies.tuples(
                    strategies.decimals(allow_nan=False, allow_infinity=False),
                    strategies.decimals(allow_nan=False, allow_infinity=False)
                ), min_size=2, max_size=2
            )
    )
    @settings(max_examples=100)
    def test_property_mae_always_geq_0(self, l):
        p, e = l

        op = isa.Operations(predicted=p , expected=e, metrics='MAE')
        res = op.compute_metrics()

        assert res >= 0

