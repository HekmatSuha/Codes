class AssemblyInterpreter:
    def __init__(self):
        self.variables = {}

    def parse_value(self, value):
        if value.endswith('h'):
            return int(value[:-1], 16)
        elif value.endswith('b'):
            return int(value[:-1], 2)
        elif value.startswith("'") and value.endswith("'"):
            return ord(value[1])
        else:
            return int(value)

    def execute(self, instructions):
        lines = instructions.strip().split('\n')
        
        # First pass: handle DB declarations
        for line in lines:
            parts = line.split(maxsplit=2)
            command = parts[1] if len(parts) > 1 else None
            if command == 'DB':
                var_name = parts[0]
                var_value = parts[2]
                self.variables[var_name] = self.parse_value(var_value)
        
        # Second pass: handle other instructions
        for line in lines:
            parts = line.split()
            command = parts[0]
            
            if command == 'DB':
                continue
            elif command == 'INC':
                var_name = parts[1]
                self.variables[var_name] += 1
            elif command == 'DEC':
                var_name = parts[1]
                self.variables[var_name] -= 1
            elif command == 'ADD':
                var_name1 = parts[1]
                var_name2 = parts[2]
                self.variables[var_name1] += self.variables[var_name2]
            elif command == 'SUB':
                var_name1 = parts[1]
                var_name2 = parts[2]
                self.variables[var_name1] -= self.variables[var_name2]
            elif command == 'MOV':
                var_name1 = parts[1]
                var_name2 = parts[2]
                self.variables[var_name1] = self.variables[var_name2]
            elif command == 'XCHG':
                var_name1 = parts[1]
                var_name2 = parts[2]
                self.variables[var_name1], self.variables[var_name2] = self.variables[var_name2], self.variables[var_name1]

    def print_variables(self):
        for var_name, var_value in self.variables.items():
            print(f"{var_name} = {var_value}")

# Example usage
interpreter = AssemblyInterpreter()
instructions = """
VAR_A DB 8
VAR_B DB 1
ADD VAR_A VAR_B
INC VAR_A
"""

interpreter.execute(instructions)
interpreter.print_variables()

