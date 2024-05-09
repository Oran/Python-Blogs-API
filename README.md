# Basic Python API Project with sqlite3

_PS. This is really poorly coded and needs a lot of work_

## Installation

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To start the server, run the following command:

Prod:

```bash
fastapi run
```

Dev:

```bash
fastapi dev
```

---

# TODOs:

- [x] **P0** Create a database with tables for users, posts, and API keys
- [x] Have a unique identifier for for api keys for each user
- [ ] **P1** Add signup and login functionality
  - [ ] Auth flow for signup and login
  - [ ] Send a token to the client and cache it in the browser
  - [ ] Cookies?
- [ ] **P3** Basic UI for the app
  - [ ] Display user profiles and posts they have made
  - [ ] Add a post
  - [ ] Delete a post
  - [ ] Edit a post
