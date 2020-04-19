import glfw
import self as self


class glfwClass:
    def __init__(self, width: int, height: int, title: str):
        if not glfw.init():
            raise Exception('nie dziala')

        self._window = glfw.create_window(width, height, title, None, None)

        if not self._window:
            glfw.terminate()
            raise Exception('window nie dziala')


        glfw.set_window_pos(self._window, 400, 200)

        glfw.make_context_current(self._window)

    def window_loop_main(self):
        while not glfw.window_should_close(self._window):
            glfw.poll_events()
            glfw.swap_buffers(self._window)

        glfw.terminate()

if __name__ == "__main__":
    window = glfwClass(800, 600, 'Overlay')
    window.window_loop_main()