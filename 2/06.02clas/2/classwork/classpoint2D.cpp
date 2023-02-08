class Point2D{
    private:
    int x,y;

    public:
    Point2D(): Point2D(0,0){}

    Point2D(const Point2D &other) : Point2D(other.x, other.y) {}

    Point2D(int x, int y){
        this->x = x;
        this->y = y;
    }

    int getX() const {
        return this->x;
    }
    int getY() const {
        return this->y;
    }
};
class Circle{
    private:
        int radius;
    public:
    Circle(): Circle(0,0){}

    Circle(const Circle &other) : Circle(other.radius) {}

    Circle(int radius)
};
int main(){

}