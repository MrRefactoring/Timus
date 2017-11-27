use std::io::{stdin};
fn main() {
    let mut input: String = String::new();
    stdin().read_line(&mut input);
    let mut numbers: Vec<&str> = input.split(" ").collect::<Vec<&str>>();
    let first: u32 = numbers[0].trim().parse().expect("type error");
    let second: u32 = numbers[1].trim().parse().expect("type error");
    println!("{}", first + second);

}
