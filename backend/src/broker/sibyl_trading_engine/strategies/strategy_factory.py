from typing import Any

from backend.src.broker.sibyl_trading_engine.strategies.bollinger_bands_strategy import (
    BollingerBandsStrategy,
)
from backend.src.broker.sibyl_trading_engine.strategies.bollinger_surge_strategy import (
    BollingerSurgeStrategy,
)
from backend.src.broker.sibyl_trading_engine.strategies.ema_crossover_strategy import (
    EMACrossoverStrategy,
)
from backend.src.broker.sibyl_trading_engine.strategies.impulse_breakout_strategy import (
    ImpulseBreakoutStrategy,
)
from backend.src.broker.sibyl_trading_engine.strategies.quantum_momentum_strategy import (
    QuantumMomentumStrategy,
)
from backend.src.broker.sibyl_trading_engine.strategies.rsi_strategy import RSIStrategy


class StrategyFactory:
    _strategies: dict[str, type] = {
        "bollinger_bands": BollingerBandsStrategy,
        "bollinger_surge": BollingerSurgeStrategy,
        "exponential_moving_average_(ema)_crossover": EMACrossoverStrategy,
        "impulse_breakout": ImpulseBreakoutStrategy,
        "quantum_momentum": QuantumMomentumStrategy,
        "rsi": RSIStrategy,
    }

    @classmethod
    def get_strategy(cls, strategy_name: str, params: dict[str, Any]) -> Any:
        strategy_class = cls._strategies.get(strategy_name)
        if not strategy_class:
            raise ValueError(f"Unknown Strategy name: {strategy_name}")
        return strategy_class(**params)
