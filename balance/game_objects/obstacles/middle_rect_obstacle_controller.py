from pygame.math import Vector2
from game_engine.time import Time
from game_engine.game_object import GameObject
from balance.game_objects.game_objects.rectangle import Rectangle
from balance.scripts.constants import Constants
from balance.game_objects.material import Material

class MiddleRectObstacleController(GameObject):

    def start(self):
        self.fall_velocity = 600
        self.game_object_list = []

    def update(self):

        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Constants.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
                GameObject.destroy(obstacle)
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                              + self.fall_velocity * Time.delta_time())
        obstacle.polygon_mesh.update_point_list(obstacle.get_points())

    def generate_obstacle(self):
        self.obstacle_width = 0.3 * Constants.screen_width
        self.obstacle_height = 0.06 * Constants.screen_height
        rect = Rectangle(Vector2(0.5 * Constants.screen_width - 0.5 * self.obstacle_width, - self.obstacle_height),
                         Vector2(self.obstacle_width, self.obstacle_height),
                         Material((255, 255, 255)))
        self.game_object_list.append(rect)
