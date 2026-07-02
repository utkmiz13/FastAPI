# How I Start Virtual Env in Macbook

**Definition of Virtual Environment:**
A virtual environment is an isolated space where you can install packages and dependencies for a specific project without affecting the global Python installation on your system.

**Hinglish:**
Virtual environment ek alag se isolated kamra hai tumhare project ke liye. Ek project ki cheezein dusre project ko kharab na karein, isliye hum har project ke liye ek alag kamra (virtual env) banate hain.

### Steps to create and start on Macbook (Terminal mein):

1. **Terminal kholo** aur apne project wale folder (directory) mein jao:
   ```bash
   cd Desktop/mera_project_folder
   ```

2. **Virtual Environment banao:**
   Yeh command ek naya folder bana dega `venv` naam se jisme is project ki saari files hongi.
   ```bash
   python3 -m venv venv
   ```

3. **Virtual Environment ko Start (Activate) karo:**
   Macbook par isko chalu karne ka command yeh hai:
   ```bash
   source venv/bin/activate
   ```
   *(Activate hone ke baad tumhare terminal mein left side par `(venv)` likha hua aayega)*

4. **Deactivate (Band) karne ke liye:**
   Jab kaam khatam ho jaye toh bas yeh likho:
   ```bash
   deactivate
   ```
