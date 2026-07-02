# Lecture 2: FastAPI & Basics

## 1. What is FastAPI?
**Definition:**
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

**Hinglish:**
FastAPI ek Python ka framework hai jiska use karke hum aasaani se aur bahot tezi se APIs bana sakte hain. Jaise ghar banane ke liye bani-banayi eent aur cement milti hai, waise hi API banane ke liye FastAPI bani-banayi tools deta hai taaki hamara kaam jaldi aur asaan ho jaye.

## 2. Philosophy of FastAPI
FastAPI ko isliye banaya gaya tha taaki:
- **Fast execution:** Ye chalne mein bahot tez ho (almost NodeJS aur Go jitna fast).
- **Fast to code:** Developers kam se kam time mein zyada kaam kar sake.
- **Fewer bugs:** Isme galtiyan (bugs) hone ke chances kam ho.
- **Easy to learn:** Naye logo ko seekhne mein asaan ho.
- **Automatic Documentation:** Ye apne aap API ka documentation bana deta hai.

## 3. What is Synchronous and Asynchronous?
**Synchronous (Sync):**
**Definition:** Operations are executed one after another. The next task cannot start until the previous one finishes.

**Hinglish:** Iska matlab hai ek ke baad ek kaam karna. Agar tum line mein khade ho, jab tak tumhare aage waale ka kaam nahi hoga, tumhara number nahi aayega. Program wait karta hai jab tak pehla task pura na ho jaye.

**Asynchronous (Async):**
**Definition:** Operations can run independently. A task can start, pause while waiting for something else, and let other tasks run in the meantime.

**Hinglish:** Iska matlab hai ki ek sath alag-alag kaam manage karna. Maan lo tumne chai banne rakhi hai. Jab tak chai ubal rahi hai, tum wait nahi karte, tum utne time mein bread toast kar lete ho. Programming mein bhi async ka use karke humara system wait nahi karta, wo background mein dusre tasks chalata rehta hai. Isse hamari API bahot fast aur smooth chalti hai.

## 4. Why FastAPI is fast to code?
FastAPI mein code karna isliye fast hai kyunki:
- **Python Type Hints:** Ye Python ke type hints use karta hai. IDE (jaise VS Code) turant bata deta hai ki kya likhna hai (auto-complete milta hai) aur agar koi galti hai toh pehle hi dikha deta hai.
- **Kam Code (Less boilerplate):** Isme tumhe faaltu ka lamba lamba setup code nahi likhna padta. Bas directly point ki baat likho aur API ready.
- **Auto-Documentation:** Tumhe API kaise use karni hai uski book (documentation) alag se nahi banani padti, FastAPI wo khud bana deta hai. Time bachta hai!
