import time

# Pipeline aşamaları
stages = ["IF", "ID", "OF", "EI", "OS"]

# Örnek komutlar
instructions = [
    "ADD R1, R2, R3",  # R1 = R2 + R3
    "SUB R4, R1, R5",  # R4 = R1 - R5 (data hazard var)
    "AND R6, R4, R7",  # R6 = R4 & R7
    "OR R8, R6, R9",   # R8 = R6 | R9
    "XOR R10, R8, R11" # R10 = R8 ^ R11
]

pipeline = []

for cycle in range(len(instructions) + len(stages)-1):
    stage_output = []
    for i in range(len(instructions)):
        stage_index = cycle - i
        if(0<=stage_index <len(stages)):
            stage_output.append(f"{instructions[i]:} --> {stages[stage_index]}")
        else:
            stage_output.append(" " * 58)

    pipeline.append(stage_output)

# Gösterim
print("Cycle-by-cycle Pipeline View:\n")
for i, stage_output in enumerate(pipeline, 1):
    print(f"Cycle {i}:")
    for line in stage_output:
        print("   ", line)
    print("-" * 50)
    time.sleep(0.5)  