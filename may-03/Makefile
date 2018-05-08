CC=gcc
CFLAGS=-Wall
WIRES_OBJ = solar-system-wires.o
RENDERED_OBJ = solar-system-rendered.o
MAIN_OBJ = main.o
LIBS=-lGL -lGLU -lglut -lm

all: wires rendered main clean

%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)

wires: $(WIRES_OBJ)
	gcc -o $@ $^ $(CFLAGS) $(LIBS)

rendered: $(RENDERED_OBJ)
	gcc -o $@ $^ $(CFLAGS) $(LIBS)

main: $(MAIN_OBJ)
	gcc -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f $(WIRES_OBJ) $(RENDERED_OBJ) $(MAIN_OBJ)
