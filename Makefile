.PHONY: check smoke

check:
	python scripts/verify_hyperbola.py --prime 17
	python scripts/verify_absorber.py --n 30 --h 5 --m 7
	python scripts/search_cycle_trades.py --prime 17 --a 1 --b 3

smoke:
	python scripts/verify_hyperbola.py --prime 11
