import numpy as np 
import argparse 


def rand_atom_positions(N: int = 1, box_size=(1.0, 1.0, 1.0)):
    box = np.array(box_size, dtype= float)

    if box.size == 1:
        box = np.repeat(box, 3)
    elif box.size != 3:
        raise ValueError("Box size must be either a single value (for cubic) or three values (for Lx, Ly, Lz).")
    
    return np.random.rand(N, 3) * box

## need to rewrite the function for printing names of different elements  while also taking in input an array of numbers one for each species n_atoms = [N0, N1, N2, ...] elements = ["H", "Li", "Mg", ...]
def print_positions(positions, elements=None):
#for i, cord in enumerate(positions): 
    for pos in positions:   
        if elements is None:
            print(f"{pos[0]:.16f} {pos[1]:.16f} {pos[2]:.16f}")
        else:
            print(f"{pos[0]:.16f} {pos[1]:.16f} {pos[2]:.16f} {elements[0]}")

    return



if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Generate random atom positions for a given number of atoms and box size.")
    parse.add_argument("--N", type = int, default=1, help="number of atoms" )
    parse.add_argument("--box", nargs="+", type=float, default=(1.0, 1.0, 1.0), help="size of the box in Lx, Ly,Lz dimensions (or single L for cubic)")
    parse.add_argument("--elements", nargs="+", type=str, default=["H"], help="list of element symbols for each atom (default: H)")


    args = parse.parse_args()

    positions = rand_atom_positions(args.N, args.box)
    print_positions(positions, args.elements)