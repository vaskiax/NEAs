class Prover():
    def __init__(self):
        self.proof = None

    
    def loader(self, path:str)  -> str:
        with open(path) as file:
            text = file.read()
        return text
    
    def  nPi(self)-> None:
        """
        This function provides a latex representation of the proof of a set of specific conditions 
        to be met by minor solar system body to be categorized as a Near Earth Asteroid (NEA). 

        The set of conditions here corresponds to the relation between the interception points of the 
        semi-major axis of the orbit of the NEA and the ones of the Earth's orbit.

        
        inputs: None

        outputs: None

        """
        from IPython.display import display, Markdown
        
        display(Markdown(
                self.loader('proofs/nPi.txt')))
        
    def tisserand(self)-> None:
        """
        This function provides a latex representation of the proof of a set of specific conditions 
        to be met by minor solar system body to be categorized as a Near Earth Asteroid (NEA). 

        The set of conditions here corresponds to the relation between the interception points of the 
        semi-major axis of the orbit of the NEA and the ones of the Earth's orbit.

        
        inputs: None

        outputs: None

        """
        from IPython.display import display, Markdown
        
        display(Markdown(
                self.loader('proofs/tisserand.txt')))
    