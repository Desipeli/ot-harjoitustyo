```mermaid
sequenceDiagram
	actor User
	participant Machine
	participant FuelTank
	participant Engine
	User->>Machine: __init__()
	Machine->>FuelTank: __init__()
	Machine->>FuelTank: fill(40)
	Machine->>Engine: __init__(FuelTank)
	
```
