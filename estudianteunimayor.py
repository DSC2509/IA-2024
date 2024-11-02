from logic import Symbol, And, Or, Not, Implication, model_check

# Definir símbolos
lluvia = Symbol("lluvia")
BBC = Symbol("BBC")
Unimayor = Symbol("Unimayor")

# Proposiciones según la diapositiva
# Proposición 1: Si no llueve, entonces los estudiantes visitan BBC
regla_lluvia_BBC = Implication(Not(lluvia), BBC)

# Proposición 2: Los estudiantes visitaron BBC o Unimayor, pero no ambos
regla_exclusiva = And(Or(BBC, Unimayor), Not(And(BBC, Unimayor)))

# Proposición 3: Se sabe que los estudiantes visitaron Unimayor
visita_unimayor = Unimayor

# Construir la base de conocimiento combinando las reglas anteriores
base_conocimiento = And(regla_lluvia_BBC, regla_exclusiva, visita_unimayor)

# Realizar inferencias
print("¿Es posible deducir que los estudiantes visitaron BBC hoy?")
print("Resultado:", model_check(base_conocimiento, BBC))

print("¿Podemos deducir que está lloviendo hoy?")
print("Resultado:", model_check(base_conocimiento, lluvia))
