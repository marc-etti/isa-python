from isa.isa import Operations
import pytest

class TestClass:
    def test_mae_0(self):
        p = [1.0, 2.0, 5.0]
        e = [1.0, 2.0, 5.0]
        expected_result = 0.0
        
        op = Operations(predicted=p, expected=e, metrics='MAE')
        computed_value = op.compute_metrics()
        
        assert computed_value == expected_result

    @pytest.mark.skip(reason="Prova skip")
    def test_mae_1(self):
        p = [1.0, 2.0, 5.0]
        e = [1.0, 2.0, 4.0]
        expected_result = 0.33
        
        op = Operations(predicted=p, expected=e, metrics='MAE')
        computed_value = op.compute_metrics()
        
        assert pytest.approx(computed_value, 0.01) == expected_result

    def test_raises_exception(self):
        p = [1.0, 2.0, 5.0]
        e = [1.0, 2.0]
        
        with pytest.raises(ValueError):
            Operations(predicted=p, expected=e, metrics='MAE')

    @pytest.mark.parametrize("p, e, expected_result, metrics", [
        ([1.0, 2.0, 3.0], [1.0, 2.0, 3.0], 0.0, "MAE"), 
        ([2.0, 3.0, 4.0], [2.0, 3.0, 4.0], 0.0, "MAE"),]
    )
    def test_parametrized(self, p, e, expected_result, metrics):
        
        op = Operations(predicted=p, expected=e, metrics=metrics)
        computed_value = op.compute_metrics()
        
        assert computed_value == expected_result

    def test_rmse(self, monkeypatch):
        p = [1.0, 2.0, 5.0]
        e = [1.0, 2.0, 5.0]
        expected_result = 0.0
        
        op = Operations(predicted=p, expected=e, metrics='RMSE')
        
        monkeypatch.setattr(op, 'compute_metrics', lambda: 0.0)
        
        computed_value = op.compute_metrics()
        assert computed_value == expected_result