from typing import List, Optional

class Question:
    def __init__(self, id: str, prompt: str, difficulty: int, choices: List[str], correct_answer: str):
        self.id = id
        self.prompt = prompt
        self.difficulty = difficulty
        self.choices = choices
        self.correct_answer = correct_answer

# Static list of questions
QUESTIONS_DB = [
    Question("q1", "What is 2 + 2?", 1, ["3", "4", "5", "6"], "4"),
    Question("q2", "Capital of France?", 1, ["London", "Paris", "Berlin", "Madrid"], "Paris"),
    Question("q18", "Elements in water?", 1, ["Hydrogen, Oxygen", "Helium, Oxygen", "Hydrogen, Nitrogen", "Carbon, Oxygen"], "Hydrogen, Oxygen"),
    Question("q21", "Color of the sky on a clear day?", 1, ["Red", "Blue", "Green", "Yellow"], "Blue"),
    Question("q22", "How many legs does a spider have?", 1, ["6", "8", "10", "4"], "8"),
    Question("q3", "What is the boiling point of water?", 2, ["90C", "100C", "110C", "120C"], "100C"),
    Question("q5", "What is the square root of 64?", 2, ["6", "7", "8", "9"], "8"),
    Question("q7", "Highest mountain in the world?", 2, ["K2", "Everest", "Kangchenjunga", "Lhotse"], "Everest"),
    Question("q14", "HTTP status code for Not Found?", 2, ["200", "404", "500", "403"], "404"),
    Question("q23", "Which planet is known as the Red Planet?", 2, ["Venus", "Mars", "Jupiter", "Saturn"], "Mars"),
    Question("q4", "Who wrote 'Hamlet'?", 3, ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"], "William Shakespeare"),
    Question("q6", "Chemical symbol for Gold?", 3, ["Ag", "Au", "Fe", "Cu"], "Au"),
    Question("q9", "Value of Pi (approx)?", 3, ["3.12", "3.14", "3.16", "3.18"], "3.14"),
    Question("q12", "Who painted the Mona Lisa?", 3, ["Van Gogh", "Da Vinci", "Picasso", "Rembrandt"], "Da Vinci"),
    Question("q24", "What gas do plants absorb?", 3, ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"], "Carbon Dioxide"),
    Question("q8", "What is part of the atom with negative charge?", 4, ["Proton", "Neutron", "Electron", "Positron"], "Electron"),
    Question("q11", "Derivate of x^2?", 4, ["x", "2x", "x^2", "2"], "2x"),
    Question("q13", "Binary for 5?", 4, ["100", "101", "110", "111"], "101"),
    Question("q19", "Solve 5! (factorial)?", 4, ["60", "100", "120", "150"], "120"),
    Question("q25", "Capital of Japan?", 4, ["Seoul", "Beijing", "Tokyo", "Bangkok"], "Tokyo"),
    Question("q10", "Speed of light (approx m/s)?", 5, ["3x10^6", "3x10^8", "3x10^10", "3x10^12"], "3x10^8"),
    Question("q16", "Complexity of Binary Search?", 5, ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "O(log n)"),
    Question("q17", "Capital of Australia?", 5, ["Sydney", "Melbourne", "Canberra", "Brisbane"], "Canberra"),
    Question("q26", "Powerhouse of the cell?", 5, ["Nucleus", "Mitochondria", "Ribosome", "Golgi"], "Mitochondria"),
    Question("q27", "Number of continents?", 5, ["5", "6", "7", "8"], "7"),
    Question("q15", "Layer 4 of OSI Model?", 6, ["Network", "Transport", "Session", "Presentation"], "Transport"),
    Question("q28", "Integral of 2x?", 6, ["x^2", "2x^2", "x", "2"], "x^2"),
    Question("q29", "First man on the moon?", 6, ["Yuri Gagarin", "Buzz Aldrin", "Neil Armstrong", "Michael Collins"], "Neil Armstrong"),
    Question("q30", "Largest ocean?", 6, ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific"),
    Question("q31", "Hardest natural substance?", 7, ["Gold", "Iron", "Diamond", "Platinum"], "Diamond"),
    Question("q32", "Who discovered Penicillin?", 7, ["Pasteur", "Fleming", "Curie", "Darwin"], "Fleming"),
    Question("q33", "Value of 'e' (approx)?", 7, ["2.17", "2.71", "3.14", "1.41"], "2.71"),
    Question("q34", "Capital of Canada?", 8, ["Toronto", "Vancouver", "Ottawa", "Montreal"], "Ottawa"),
    Question("q35", "Smallest prime number?", 8, ["0", "1", "2", "3"], "2"),
    Question("q36", "Start of WWI?", 8, ["1912", "1914", "1918", "1939"], "1914"),
    Question("q37", "Process of water to gas?", 9, ["Condensation", "Evaporation", "Sublimation", "Precipitation"], "Evaporation"),
    Question("q38", "Atomic number of Carbon?", 9, ["4", "6", "8", "12"], "6"),
    Question("q39", "Distance to Sun (approx AU)?", 9, ["1", "10", "100", "0.1"], "1"),
    Question("q20", "Year expected for simple implementation?", 10, ["2024", "2025", "2026", "Infinity"], "2026"),
    Question("q40", "Speed of sound in air (approx)?", 10, ["300 m/s", "343 m/s", "1000 m/s", "3x10^8 m/s"], "343 m/s"),
    Question("q41", "Is P=NP?", 10, ["Yes", "No", "Unproven", "42"], "Unproven"),
    Question("q42", "What is the capital of Egypt?", 6, ["Cairo", "Alexandra", "Giza", "Luxor"], "Cairo"),
    Question("q43", "Who proposed the Theory of Relativity?", 6, ["Newton", "Einstein", "Galileo", "Bohr"], "Einstein"),
    Question("q44", "How many bones in human body?", 7, ["200", "206", "210", "212"], "206"),
    Question("q45", "Lightest element?", 7, ["Helium", "Hydrogen", "Lithium", "Boron"], "Hydrogen"),
    Question("q46", "Who wrote '1984'?", 7, ["Orwell", "Huxley", "Bradbury", "Steinbeck"], "Orwell"),
    Question("q47", "Capital of Brazil?", 7, ["Rio de Janeiro", "Sao Paulo", "Brasilia", "Salvador"], "Brasilia"),
    Question("q48", "Square root of 256?", 8, ["12", "14", "16", "18"], "16"),
    Question("q49", "Atomic number of Gold?", 8, ["50", "79", "80", "100"], "79"),
    Question("q50", "Year the Berlin Wall fell?", 8, ["1987", "1989", "1991", "1993"], "1989"),
    Question("q51", "Largest planet in solar system?", 8, ["Saturn", "Jupiter", "Neptune", "Uranus"], "Jupiter"),
    Question("q52", "Who painted 'Starry Night'?", 8, ["Monet", "Van Gogh", "Dali", "Munch"], "Van Gogh"),
    Question("q53", "Chemical symbol for Tungsten?", 9, ["T", "Tu", "W", "Tg"], "W"),
    Question("q54", "What is the 10th prime number?", 9, ["23", "29", "31", "37"], "29"),
    Question("q55", "Capital of Turkey?", 9, ["Istanbul", "Ankara", "Izmir", "Bursa"], "Ankara"),
    Question("q56", "In which year did Titanic sink?", 9, ["1910", "1912", "1914", "1915"], "1912"),
    Question("q57", "How many hearts does an octopus have?", 9, ["1", "2", "3", "4"], "3"),
    Question("q58", "Speed of sound in water (approx)?", 9, ["343 m/s", "1480 m/s", "3000 m/s", "5000 m/s"], "1480 m/s"),
    Question("q59", "Planck's Constant (approx)?", 10, ["6.626e-34", "3.14159", "1.602e-19", "9.81"], "6.626e-34"),
    Question("q60", "First Turing Award winner?", 10, ["Alan Perlis", "Maurice Wilkes", "Richard Hamming", "Marvin Minsky"], "Alan Perlis"),
    Question("q61", "Number of keys on standard piano?", 10, ["66", "72", "88", "101"], "88"),
    Question("q62", "Capital of Kazakhstan?", 10, ["Almaty", "Astana", "Tashkent", "Bishkek"], "Astana"),
    Question("q63", "Distance to Moon (approx km)?", 10, ["100,000", "250,000", "384,400", "500,000"], "384,400"),
    Question("q64", "Melting point of Tungsten?", 10, ["1500C", "2000C", "3422C", "5000C"], "3422C"),
    Question("q65", "Who discovered the electron?", 10, ["Rutherford", "Bohr", "Thomson", "Chadwick"], "Thomson")
]

class QuestionRepository:
    def get_question_by_id(self, question_id: str) -> Optional[Question]:
        for q in QUESTIONS_DB:
            if q.id == question_id:
                return q
        return None

    def get_questions_by_difficulty(self, difficulty: int) -> List[Question]:
        # Simple implementation: Return all match, random selection handling in service
        return [q for q in QUESTIONS_DB if q.difficulty == difficulty]
    
    def get_all_questions(self):
        return QUESTIONS_DB

question_repo = QuestionRepository()
