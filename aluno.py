class Aluno:
    alunos = []
    def __init__(self, nome, curso, ano):
        self._nome = nome
        self._curso = curso
        self._ano = ano
        Aluno.alunos.append(self)
    
    def __str__(self):
        return f'Nome: {self._nome} | Curso: {self._curso} | Ano: {self.ano}'
    
    @property
    def ano(self):
        return f'{self._ano}° Ano'
    
    @classmethod
    def listar_alunos(cls):
        print(f'{"Nome do aluno".ljust(20)} | {"Curso".ljust(20)} | {"Ano".ljust(20)}')
        print(60 * '-')
        for i in cls.alunos:
            print(f'{i._nome.ljust(20)} | {i._curso.ljust(20)} | {i.ano.ljust(20)}')
    