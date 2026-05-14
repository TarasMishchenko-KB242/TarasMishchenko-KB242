/**
 * Клас Point для координат
 */
class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    toString() {
        return `(${this.x},${this.y})`;
    }
}

/**
 * Базовий "Абстрактний" клас Figure
 */
class Figure {
    constructor() {
        if (this.constructor === Figure) {
            throw new Error("Неможливо створити екземпляр абстрактного класу Figure.");
        }
    }

    // Абстрактні методи
    area() {
        throw new Error("Метод area() має бути реалізований.");
    }

    centroid() {
        throw new Error("Метод centroid() має бути реалізований.");
    }

    toString() {
        throw new Error("Метод toString() має бути реалізований.");
    }
}

/**
 * Клас Triangle (Трикутник)
 */
class Triangle extends Figure {
    constructor(a, b, c) {
        super();
        this.a = a;
        this.b = b;
        this.c = c;

        if (this.area() <= 0) {
            throw new Error("Трикутник вироджений (точки лежать на одній прямій або збігаються).");
        }
    }

    area() {
        // Формула Герона через координати
        return Math.abs(
            (this.a.x * (this.b.y - this.c.y) +
             this.b.x * (this.c.y - this.a.y) +
             this.c.x * (this.a.y - this.b.y)) / 2
        );
    }

    centroid() {
        return new Point(
            (this.a.x + this.b.x + this.c.x) / 3,
            (this.a.y + this.b.y + this.c.y) / 3
        );
    }

    toString() {
        return `Triangle[A${this.a} B${this.b} C${this.c}]`;
    }
}

/**
 * Клас Quadrilateral (Чотирикутник)
 */
class Quadrilateral extends Figure {
    constructor(a, b, c, d) {
        super();
        this.points = [a, b, c, d];

        if (this.area() <= 0) {
            throw new Error("Чотирикутник вироджений або самоперетинний.");
        }
    }

    area() {
        // Формула Гаусса (Shoelace formula)
        let area = 0;
        let j = this.points.length - 1;
        for (let i = 0; i < this.points.length; i++) {
            area += (this.points[j].x + this.points[i].x) * (this.points[j].y - this.points[i].y);
            j = i;
        }
        return Math.abs(area / 2);
    }

    centroid() {
        // Центроїд площі для багатокутника
        let cx = 0, cy = 0;
        let area = 0;
        for (let i = 0; i < this.points.length; i++) {
            let next = (i + 1) % this.points.length;
            let factor = (this.points[i].x * this.points[next].y - this.points[next].x * this.points[i].y);
            cx += (this.points[i].x + this.points[next].x) * factor;
            cy += (this.points[i].y + this.points[next].y) * factor;
            area += factor;
        }
        area /= 2;
        let f = 6 * area;
        return new Point(cx / f, cy / f);
    }

    toString() {
        return `Quadrilateral[A${this.points[0]} B${this.points[1]} C${this.points[2]} D${this.points[3]}]`;
    }
}

/**
 * Клас Circle (Коло)
 */
class Circle extends Figure {
    constructor(center, radius) {
        super();
        if (radius <= 0) {
            throw new Error("Радіус має бути більше нуля.");
        }
        this.center = center;
        this.radius = radius;
    }

    area() {
        return Math.PI * Math.pow(this.radius, 2);
    }

    centroid() {
        return this.center; // Центроїд кола - це його центр
    }

    toString() {
        return `Circle[${this.center} Radius:${this.radius}]`;
    }
}

// === ТЕСТУВАННЯ ===

try {
    console.log("--- Тест Трикутника ---");
    const t = new Triangle(new Point(0, 0), new Point(4, 0), new Point(0, 3));
    console.log(t.toString());
    console.log("Площа:", t.area());
    console.log("Центроїд:", t.centroid().toString());

    console.log("\n--- Тест Чотирикутника (Квадрат) ---");
    const q = new Quadrilateral(new Point(0, 0), new Point(4, 0), new Point(4, 4), new Point(0, 4));
    console.log(q.toString());
    console.log("Площа:", q.area());
    console.log("Центроїд:", q.centroid().toString());

    console.log("\n--- Тест Кола ---");
    const c = new Circle(new Point(5, 5), 10);
    console.log(c.toString());
    console.log("Площа:", c.area().toFixed(2));
    console.log("Центроїд:", c.centroid().toString());

    // Тест помилки (вироджена фігура)
    // console.log("\n--- Тест Помилки ---");
    // const wrongTriangle = new Triangle(new Point(0,0), new Point(1,1), new Point(2,2));

} catch (e) {
    console.error("Помилка:", e.message);
}