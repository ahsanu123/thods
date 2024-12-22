#include <armadillo>
#include <iostream>
#include <ncurses.h>

using namespace std;
using namespace arma;

int main(int argc, char **argv) {

  mat A(4, 5, fill::randu);
  mat B(4, 5, fill::randu);

  initscr();
  A.print();
  printw("Hello Fucking World");
  refresh();
  getch();
  endwin();

  return 0;
}
