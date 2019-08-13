#include <stdio.h>

typedef struct
{
    /* data */
    int x;
    int y;
}Point;

typedef struct
{
    /* data */
    Point pos;
    int dir;

}PDData;

PDData lgv[3];

int main(int argc, char const *argv[])
{
    /* code */
    lgv[0].pos.x = 10;
    lgv[0].pos.y = 10;
    lgv[0].dir = 30;

    lgv[1].pos.x = 10;
    lgv[1].pos.y = 20;
    lgv[1].dir = 60;

    lgv[2].pos.x = 30;
    lgv[2].pos.y = 10;
    lgv[2].dir = 90;

    for (int i = 0; i < 3; i++) {
        printf("lgv[%d], pos=(%d,%d), dir=%d\n", i, lgv[i].pos.x, lgv[i].pos.y, lgv[i].dir);
    }


    PDData *tmp;
    for (int i = 0; i < 3; i++) {
        tmp = &lgv[i];
        printf("lgv[%d], pos=(%d,%d), dir=%d\n", i, tmp->pos.x, tmp->pos.y, tmp->dir);
    }
        


    return 0;
}
