from rdkit import Chem
from mordred import descriptors, Calculator
import argparse


def sdf2mol(sdf_path):
    suppl = Chem.SDMolSupplier(sdf_path)
    smiles, mols, indexes = [], [], []
    for i in range(len(suppl)):
        mol = suppl[i]
        if mol is not None:
            smi = Chem.MolToSmiles(mol)
            smiles.append(smi)
            indexes.append(i)
            mols.append(mol)
    return (mols, smiles, indexes)


def calc_mordred(mols, smiles, indexes, ignore_3D):
    global calc
    if ignore_3D:
        calc = Calculator(descriptors, ignore_3D=True)
    else:
        calc = Calculator(descriptors)
    # calculate descriptors
    df_mord = calc.pandas(mols)
    df_mord = df_mord.astype(str)
    masks = df_mord.apply(
        lambda d: d.str.contains('[a-zA-Z]', na=False))
    df_mord = df_mord[~masks]
    df_mord = df_mord.astype(float)
    # reset index
    df_mord.insert(0, 'SMILES', smiles)
    df_mord.insert(0, 'index', indexes)
    df_mord = df_mord.set_index('index')
    return df_mord


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('sdf_path')
    parser.add_argument('--ignore_3D', action='store_true')
    args = parser.parse_args()

    # load sdf and calculate mordred descriptors
    mols, smiles, indexes = sdf2mol(args.sdf_path)
    result = calc_mordred(mols, smiles, indexes, args.ignore_3D)
    
    # save files
    f_name = args.sdf_path.split('.')[0] + '_mordred.csv'
    result.to_csv(f_name)







