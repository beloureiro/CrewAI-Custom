import os
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama  # Importa o módulo Ollama para usar modelos locais

# 1. Configuração da chave da API do OpenAI
# Define a chave da API do OpenAI, necessária para acessar os modelos da OpenAI.
os.environ["OPENAI_API_KEY"] = "SUA_CHAVE_API_AQUI"

# 2. Configuração do modelo local com Ollama
# Configura um modelo local usando Ollama, que permite usar modelos de linguagem diretamente no seu computador.
ollama_model = Ollama(model="openhermes")

# 3. Criação do agente "Researcher" (Pesquisador)
# Este agente é responsável por pesquisar novas tendências em IA.
# As seguintes propriedades podem ser personalizadas:
# - role: Nome do papel do agente.
# - goal: Objetivo específico do agente.
# - backstory: Contexto ou "história de fundo" do agente, que influencia seu comportamento.
researcher = Agent(
    role='Researcher',
    goal='Research new AI insights',
    backstory="You are an AI research assistant.",
    verbose=True,  # Exibe informações detalhadas durante a execução.
    allow_delegation=False,  # Impede que o agente delegue tarefas a outros.
    llm=ollama_model  # Usa o modelo local configurado com Ollama.
)

# 4. Criação do agente "Writer" (Escritor)
# Este agente é responsável por escrever um post de blog baseado nas descobertas do pesquisador.
# As mesmas propriedades (role, goal, backstory) podem ser personalizadas como no agente anterior.
writer = Agent(
    role='Writer',
    goal='Write compelling and engaging blog posts about AI trends and insights.',
    backstory="You are an AI blog post writer who specializes in writing about AI topics.",
    verbose=True,
    allow_delegation=False,
    llm=ollama_model
)

# 5. Definição das tarefas (Tasks)
# Define as tarefas que cada agente deve realizar.
# Cada tarefa tem uma descrição e um agente responsável por executá-la.
# - description: O que a tarefa deve realizar.
# - expected_output: O resultado esperado da tarefa.
task1 = Task(
    description="Investigate the latest AI trends.",
    expected_output="Detailed report on AI trends.",
    agent=researcher
)

task2 = Task(
    description="Write a compelling blog post based on the latest AI trends.",
    expected_output="A well-written blog post about AI trends.",
    agent=writer
)

# 6. Instanciação da equipe (Crew)
# Cria a equipe que vai executar as tarefas. A equipe inclui os agentes definidos e as tarefas atribuídas.
# - agents: Lista de agentes na equipe.
# - tasks: Lista de tarefas a serem executadas.
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True,  # Define se exibe mensagens detalhadas durante a execução.
    process=Process.sequential  # As tarefas serão executadas em sequência.
)

# 7. Execução do processo
# Inicia a execução das tarefas pela equipe.
result = crew.kickoff()

# 8. Impressão dos resultados
# Exibe o resultado final das tarefas executadas pela equipe.
print(result)
