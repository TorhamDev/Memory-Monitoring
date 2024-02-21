from datetime import datetime

import psutil

from src.schema import MemoryStatistics


def collect_memory_metrics() -> MemoryStatistics:
    ram = psutil.virtual_memory()

    return MemoryStatistics(
        date=datetime.now(),
        used=ram.used,
        free=ram.free,
        total=ram.total,
    )
