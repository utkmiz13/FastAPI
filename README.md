# FastAPI Roadmap (My Notes)

```mermaid
graph TD;
    A[Phase 1: Basics & Setup] --> B[Phase 2: Core Concepts]
    B --> C[Phase 3: Database]
    C --> D[Phase 4: Security]
    D --> E[Phase 5: Deployment]

    subgraph A [Phase 1: Basics & Setup]
        a1(API & FastAPI Basics)
        a2(Sync vs Async)
        a3(Virtual Env Setup)
        a4(Correct Import Syntax)
    end

    subgraph B [Phase 2: Core Concepts]
        b1(Path & Query Parameters)
        b2(Pydantic Models)
        b3(Data Validation)
    end

    subgraph C [Phase 3: Database]
        c1(SQLAlchemy Setup)
        c2(CRUD Operations)
        c3(APIRouter Structure)
    end

    subgraph D [Phase 4: Security]
        d1(Middleware & CORS)
        d2(JWT Authentication)
        d3(Background Tasks)
    end

    subgraph E [Phase 5: Deployment]
        e1(Docker)
        e2(Cloud Deployment)
    end
```

## Existing Notes
- [What is an API?](Lecture_1_What_is_an_API/notes.md)
- [FastAPI Basics](Lecture_2_FastAPI_Basics/notes.md)
- [How to start virtual env in Macbook](How_to_start_virtual_env_macbook/notes.md)
- [Correct API Import Syntax](How_to_import_API_correct_syntax/notes.md)
