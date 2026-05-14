// Допоміжний клас Point для представлення точок на площині
class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    toString() {
        return `(${this.x.toFixed(2)}; ${this.y.toFixed(2)})`;
    }
}

// === Завдання 1: Клас Line (Пряма) ===
class Line {
    constructor(k, b) {
        this.k = k;
        this.b = b;
    }

    intersection(other) {
        // Якщо коефіцієнти нахилу однакові, лінії паралельні (або збігаються)
        if (this.k === other.k) {
            return null;
        }
        // Розрахунок x: k1*x + b1 = k2*x + b2 => x = (b2 - b1) / (k1 - k2)
        const x = (other.b - this.b) / (this.k - other.k);
        const y = this.k * x + this.b;
        return new Point(x, y);
    }
}

// === Завдання 2: Клас Segment (Відрізок) ===
class Segment {
    constructor(start, end) {
        // Перевірка на виродженість
        if (start.x === end.x && start.y === end.y) {
            throw new Error("Відрізок вироджений: початок і кінець збігаються.");
        }
        this.start = start;
        this.end = end;
    }

    length() {
        return Math.sqrt(
            Math.pow(this.end.x - this.start.x, 2) + 
            Math.pow(this.end.y - this.start.y, 2)
        );
    }

    middle() {
        return new Point(
            (this.start.x + this.end.x) / 2,
            (this.start.y + this.end.y) / 2
        );
    }

    intersection(another) {
        const x1 = this.start.x, y1 = this.start.y;
        const x2 = this.end.x, y2 = this.end.y;
        const x3 = another.start.x, y3 = another.start.y;
        const x4 = another.end.x, y4 = another.end.y;

        const den = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1);
        if (den === 0) return null; // Паралельні

        const ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / den;
        const ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / den;

        // Перевірка, чи точка лежить саме на відрізках (0 <= u <= 1)
        if (ua >= 0 && ua <= 1 && ub >= 0 && ub <= 1) {
            return new Point(x1 + ua * (x2 - x1), y1 + ua * (y2 - y1));
        }
        return null;
    }
}

// === Завдання 3: Клас Triangle (Трикутник) ===
class Triangle {
    constructor(a, b, c) {
        this.a = a;
        this.b = b;
        this.c = c;
        
        if (this.area() === 0) {
            throw new Error("Трикутник не існує (точки лежать на одній прямій).");
        }
    }

    area() {
        // Площа за координатами вершин
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
}

// === ТЕСТУВАННЯ ЗАВДАНЬ ===

console.log("--- Завдання 1 (Line) ---");
const line1 = new Line(1, 1);
const line2 = new Line(-1, 3);
const lineIntersect = line1.intersection(line2);
console.log(`Точка перетину прямих: ${lineIntersect ? lineIntersect.toString() : "null"}`); 
// Очікувано: (1.00; 2.00)

console.log("\n--- Завдання 2 (Segment) ---");
const p1 = new Point(0, 0), p2 = new Point(4, 4);
const p3 = new Point(0, 4), p4 = new Point(4, 0);
const seg1 = new Segment(p1, p2);
const seg2 = new Segment(p3, p4);

console.log(`Довжина сегмента 1: ${seg1.length().toFixed(2)}`);
console.log(`Середина сегмента 1: ${seg1.middle().toString()}`);
console.log(`Перетин сегментів: ${seg1.intersection(seg2).toString()}`); 
// Очікувано: (2.00; 2.00)

console.log("\n--- Завдання 3 (Triangle) ---");
try {
    const tA = new Point(0, 0), tB = new Point(4, 0), tC = new Point(0, 3);
    const triangle = new Triangle(tA, tB, tC);
    console.log(`Площа трикутника: ${triangle.area()}`);
    console.log(`Центроїд трикутника: ${triangle.centroid().toString()}`);
} catch (error) {
    console.error(error.message);
}