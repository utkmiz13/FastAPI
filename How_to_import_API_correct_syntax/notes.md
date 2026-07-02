# How to Import the API - Correct Syntax

Jab tum FastAPI use karte ho, toh sabse pehle usko apne Python code mein import (lana) padta hai.

### Sahi Syntax (Correct Syntax):

```python
from fastapi import FastAPI

# Ek 'app' naam ka instance (object) banate hain
app = FastAPI()

# Ab is app ka use karke hum routes (rasta) banate hain
@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

**Hinglish me samjho:**
- `from fastapi` ka matlab hai "fastapi library se"
- `import FastAPI` ka matlab hai "FastAPI tool ko le aao"

**Dhyaan rakhne wali baat (Common Mistake):**
Log galti se `import fastapi` karke direct use karne lagte hain, jo ki galat hai. 
Sahi tareeka yahi hai ki `FastAPI` (jisme 'F' aur 'API' capital hain) ko explicitly import karo jaise upar likha hai. Phir uska ek object banao `app = FastAPI()`. Yahi `app` tumhara main engine hoga jo saari API requests handle karega.
