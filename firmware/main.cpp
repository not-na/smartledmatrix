#include "main.h"

int main()
{
    stdio_init_all();

    // Binary info
    bi_decl(bi_program_description("Smart 64x64 LED HUB75 Matrix firmware, controlled via a Pi Zero 2 W"));
    bi_decl(bi_program_name("smartledmatrix-firmware"));

    hub75_init();

    multicore_launch_core1(hub75_main);
    sleep_ms(100);

    while (true) {
        printf("!READY\n");
        sleep_ms(100);

        // TODO: wait for host ready
    }

    // TODO: UART recv main loop
}
