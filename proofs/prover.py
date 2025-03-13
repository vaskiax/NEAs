class Prover():
    def __init__(self, name=None):
        self.proof = name
    
    def  nPi(self):
        with open('proofs/nPi.txt') as file:
            from IPython.display import Markdown, display
            full_text = file.read()
            display(Markdown(full_text))
    