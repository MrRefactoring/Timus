use std::io::{stdin};

fn read_int() -> u32{
    let mut input: String = String::new();
    stdin().read_line(&mut input).expect("input error");
    return input.trim().parse().expect("type error");
}

fn read_line() -> String{
    let mut input: String = String::new();
    stdin().read_line(&mut input);
    return input;
}

fn main(){
    let number: u32 = read_int();
    let mut count: usize = 2;
    for i in 0..number {
        let input = read_line();
        let mut people: Vec<&str> = input.split("+").collect::<Vec<&str>>();
        count += people.len();
    }
    if count == 13{
        println!("{}", (count + 1) * 100);
    } else {
        print!("{}", count * 100);
    }
}
