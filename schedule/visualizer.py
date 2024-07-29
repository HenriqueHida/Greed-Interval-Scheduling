import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import defaultdict
import numpy as np

# Define a class structure
class Class:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        self.classroom = None  # To be assigned

# More classes with varied and overlapping schedules
classes = [
    Class('Math', 9, 10),
    Class('Science', 10, 11),
    Class('English', 11, 13),
    Class('History', 13, 14),
    Class('Art', 14, 15),
    Class('Biology', 10, 12),
    Class('Chemistry', 15, 16),
    Class('Physics', 15, 17),
    Class('Music', 16, 17),
    Class('Drama', 9, 10),
    Class('Sports', 10, 11),
    Class('Geography', 12, 14),
    Class('Economics', 13, 14),
    Class('Philosophy', 9, 10),
    Class('Software', 14, 16)
]

# Define the number of classrooms
num_classrooms = 3

# Function to animate the scheduling process
def animate_scheduling_process(classes, num_classrooms):
    fig, ax = plt.subplots(figsize=(12, 6))
    classrooms = [0] * num_classrooms
    class_colors = {cls.name: np.random.rand(3,) for cls in classes}

    # Sort classes by end time (Greedy approach)
    sorted_classes = sorted(classes, key=lambda x: x.end)

    def init():
        ax.set_xlim(8, 18)
        ax.set_ylim(0.5, num_classrooms + 0.5)
        ax.set_xlabel('Time')
        ax.set_ylabel('Classroom')
        ax.set_title('Class Scheduling Process')
        ax.set_xticks(range(8, 19))
        ax.set_yticks(range(1, num_classrooms + 1))
        ax.set_yticklabels([f'Classroom {i+1}' for i in range(num_classrooms)])
        ax.grid(True)
        plt.subplots_adjust(left=0.125, bottom=0.11, right=0.75, top=0.88, wspace=0.2, hspace=0.2)
        handles = [plt.Rectangle((0,0),1,1, color=class_colors[cls.name]) for cls in classes]
        labels = [f"{cls.name}: {cls.start}-{cls.end}" for cls in classes]
        ax.legend(handles, labels, title="Class Schedules", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
        return ax,

    def update(frame):
        ax.clear()
        init()
        current_class = sorted_classes[frame]
        assigned = False

        # Assign the class to the first available classroom
        for i in range(num_classrooms):
            if classrooms[i] <= current_class.start:
                current_class.classroom = i + 1
                classrooms[i] = current_class.end
                assigned = True
                break

        for class_ in sorted_classes[:frame + 1]:
            if class_.classroom is not None:
                color = class_colors[class_.name]
                ax.broken_barh([(class_.start, class_.end - class_.start)],
                               (class_.classroom - 0.4, 0.8),
                               facecolors=color)
                ax.text(class_.start + (class_.end - class_.start) / 2,
                        class_.classroom, class_.name, va='center',
                        ha='center', color='black', fontsize=8)

        if assigned:
            ax.arrow(current_class.start, current_class.classroom,
                     current_class.end - current_class.start, 0,
                     head_width=0.2, head_length=0.1,
                     fc='green', ec='green')

        return ax,

    ani = FuncAnimation(fig, update, frames=len(sorted_classes), init_func=init, blit=True, repeat=False)
    plt.show()

# Animate the scheduling process
animate_scheduling_process(classes, num_classrooms)
