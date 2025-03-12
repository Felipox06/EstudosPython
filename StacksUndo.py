#LIFO (last in first out)

class EditorTexto:
    def __init__(self):
        self.texto = ""
        self.stack_undo = []
        
    def inserir(self, texto_novo):
        self.texto += texto_novo
        self.stack_undo.append(self.texto)
        print(f"O texto está assim: {self.texto}")
        
    def undo(self):
        if self.stack_undo:
            self.texto = self.stack_undo.pop()
            print(f"Undo: {self.texto}")
        else:
            print("Nada para desfazer")
            
# Teste
editor = EditorTexto()
editor.inserir("Olá, ")
editor.inserir("mundo!")
editor.undo()
editor.undo()