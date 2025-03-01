from shapes import Triangle, Rectangle, Trapeze, Parallelogram, Circle


def read_shapes_from_file(filename):
    shapes = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if not parts:
                continue
            shape_type = parts[0]
            params = list(map(float, parts[1:]))
            try:
                if shape_type == "Triangle":
                    shapes.append(Triangle(*params))
                elif shape_type == "Rectangle":
                    shapes.append(Rectangle(*params))
                elif shape_type == "Trapeze":
                    shapes.append(Trapeze(*params))
                elif shape_type == "Parallelogram":
                    shapes.append(Parallelogram(*params))
                elif shape_type == "Circle":
                    shapes.append(Circle(*params))
            except ValueError as e:
                print(f"Помилка при створенні фігури {shape_type} з параметрами {params}: {e}")
    return shapes


def find_max_area_and_perimeter(shapes):
    if not shapes:
        raise ValueError("Список фігур порожній.")
    max_area_shape = max(shapes, key=lambda shape: shape.area())
    max_perimeter_shape = max(shapes, key=lambda shape: shape.perimeter())
    return max_area_shape, max_perimeter_shape


def write_results_to_file(filename, max_area_shape, max_perimeter_shape):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("Фігура з найбільшою площею:\n")
            file.write(str(max_area_shape) + "\n\n")
            file.write("Фігура з найбільшим периметром:\n")
            file.write(str(max_perimeter_shape) + "\n")
        print(f"Результати успішно збережено у файл '{filename}'.")
    except Exception as e:
        print(f"Помилка при записі результатів у файл: {e}")


def main():
    input_filename = "input.txt"
    output_filename = "output.txt"

    # Зчитування фігур з файлу
    shapes = read_shapes_from_file(input_filename)

    # Перевірка, чи є фігури у списку
    if not shapes:
        print("Увага: список фігур порожній. Перевірте вхідний файл.")
        return

    try:
        # Знаходження фігур з найбільшою площею та периметром
        max_area_shape, max_perimeter_shape = find_max_area_and_perimeter(shapes)

        # Виведення результатів у консоль
        print("Фігура з найбільшою площею:")
        print(max_area_shape)
        print("\nФігура з найбільшим периметром:")
        print(max_perimeter_shape)

        # Запис результатів у файл
        write_results_to_file(output_filename, max_area_shape, max_perimeter_shape)
    except ValueError as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()