### Pouziti

#### 1. Instalace pomoci makefile

1. **po spusteni make se vytvori venv kde jsou nainstalovane balicky a spusti se aplikace v tomto prostredi. Priste staci jen spustit make a aplikace se spusti**

   ```bash
   git clone <url_projektu>
   cd <adresar_projektu>
   make
   ```

#### 2. Rucni instalace

1. **Rucni instalace pri prvnim spusteni je treba nainstalovat balicky do venv.**
   ```bash
    git clone <url_projektu>
    cd <adresar_projektu>
    python3.11 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cp .env.dev .env
    python3.11 src/main.py
   ```
2. **pristi spusteni**
   ```bash
   source venv/bin/activate
   python3.11 src/main.py
   ```

#### 3. Instalace pomoci dockeru

1. **po spusteni make se vytvori venv kde jsou nainstalovane balicky a spusti se aplikace v tomto prostredi. Priste staci jen spustit make a aplikace se spusti**

   ```bash
   git clone <url_projektu>
   cd <adresar_projektu>
   make docker
   ```

   1. **Neni potreba mit nainstalovany python, pip**
   2. **Snadna instalace**
   3. **Prihodil jsem i PgAdmin na localhost:8888 jednoduche prohlizeni db**
   4. **Pripravnena prazdna postgres db**
   5. **Do Makefilu jsem popsal zakladni pouziti pres command line at to nemusite hledat**

### Zdroje na instalaci pro rucni instalaci verze 3.11

1. [Instalace pythonu](https://www.python.org/downloads/)
2. Pokud se vydate cestou pres makefile tak nemam paru jestli to bezi na windowsich nicmene na linuxu a mecu je nejspis defaultne nainstalovany

3. [Instalace dockeru](https://docs.docker.com/engine/install/)
4. [Instalace docker compose](https://docs.docker.com/compose/install/)
5. Makefile nemusite myt nainstalovany muzete spoustet primo docker commandy z console staci si je skopirovat bez @
   funkcionalita je stejna Makefile je jen takova berlicka ktera to trosku usnadnuje.

### Nejaky info k dockeru

https://www.baeldung.com/cs/virtualization-vs-containerization
