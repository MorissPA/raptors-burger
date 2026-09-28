# Instrukcja instalacji i konfiguracji środowiska symulacyjnego


## 1. Wymagania systemowe

Do poprawnego działania środowiska wymagane są:
System operacyjny: Ubuntu 24.04 LTS (instalacja natywna, wirtualizowana lub WSL2).
Środowisko bazowe: ROS 2 Jazzy Jalisco (zalecana instalacja typu `desktop`). W przypadku braku środowiska należy postępować zgodnie z [oficjalną dokumentacją ROS 2](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html).

## 2. Instalacja zależności

Przed pobraniem kodu źródłowego należy zainstalować niezbędne narzędzia budowania, symulator Gazebo oraz bazowe pakiety TurtleBot3. Należy wykonać poniższe polecenia w terminalu:

```bash
sudo apt update
sudo apt install python3-colcon-common-extensions
sudo apt install ros-jazzy-gazebo-ros-pkgs ros-jazzy-turtlebot3-msgs ros-jazzy-navigation2 ros-jazzy-nav2-bringup ros-jazzy-turtlebot3-gazebo
```

## 3. Konfiguracja przestrzeni roboczej

Rozwiązania zadań powinny być implementowane we własnej kopii repozytorium (tzw. fork) na gałęzi simulation.

Należy utworzyć przestrzeń roboczą (workspace) i pobrać repozytorium:

```bash
mkdir -p ~/raptors_ws/src
cd ~/raptors_ws/src
```

#### Uwaga: Należy podmienić poniższy adres na link do własnego forka repozytorium

```bash
git clone [https://github.com/](https://github.com/)<NAZWA_UZYTKOWNIKA>/raptors-burger.git
cd raptors-burger
git checkout -b rekrutacja-<imie>-<nazwisko>
```

##4. Budowanie pakietów

Aby skompilować pakiety w przestrzeni roboczej, należy użyć narzędzia colcon z poziomu katalogu głównego (workspace):

```bash
cd ~/raptors_ws
colcon build --symlink-install
```

Po zakończeniu budowania konieczne jest przeładowanie środowiska:

```bash
source install/setup.bash
```

## 5. Uruchomienie symulacji

W celu uruchomienia symulacji, system wymaga zdefiniowania modelu robota poprzez zmienną środowiskową TURTLEBOT3_MODEL. Zmienną tę należy zadeklarować w każdym nowym oknie terminala lub dodać na stałe do pliku .bashrc.

Terminal 1: Uruchomienie środowiska Gazebo

```bash
export TURTLEBOT3_MODEL=burger
source ~/raptors_ws/install/setup.bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Terminal 2: Uruchomienie węzła sterowania (Teleop)

```bash
export TURTLEBOT3_MODEL=burger
source ~/raptors_ws/install/setup.bash
ros2 run turtlebot3_teleop teleop_keyboard
```

Sterowanie wirtualnym robotem odbywa się za pomocą klawiszy W, A, S, D, X po aktywowaniu okna Terminala 2.

## 6. Konfiguracja opcjonalna (Zmienne środowiskowe)

Aby uniknąć konieczności definiowania ścieżek oraz modelu robota przy każdym uruchomieniu terminala, zaleca się dodanie poniższych wpisów do pliku konfiguracyjnego powłoki:

```bash
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
echo "source ~/raptors_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
