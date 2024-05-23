import pytest

import isa.isa as isa

class TestIntegration:
    
    def test_integration_arguments(self, monkeypatch):
        import argparse

        def return_value() -> argparse.Namespace:
            return argparse.Namespace(
                predicted=[1.0, 2.0, 3.0], 
                expected=[1.0, 2.0, 3.0], 
                metrics='MAE'
            )

        monkeypatch.setattr(isa, 'setup_parser', return_value)

        assert isa.main(isa.setup_parser()) == 0