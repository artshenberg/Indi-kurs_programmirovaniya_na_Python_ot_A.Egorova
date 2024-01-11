"""
Превращаем вложенный словарь в плоский
Перед вами имеется вложенный словарь, уровень вложенности произвольный и заранее неизвестен. Ключами словаря на любом
уровне могут быть только строки, значения - только числа.

Учитывая указанные выше условия, ваша задача состоит в том, чтобы преобразовать этот вложенный словарь в плоский
(состоящий только из одного уровня), где ключи формируются конкатенацией вложенных ключей, соединенных знаком _

Для этого необходимо определить рекурсивную функцию flatten_dict. Она должна принимать вложенный словарь и возвращать
плоский

Ниже приведены несколько способов решения вышеуказанной задачи.

nested = {'Germany': {'berlin': 7},
          'Europe': {'italy': {'Rome': 3}},
          'USA': {'washington': 1, 'New York': 4}}

flatten_dict(nested) => {'Germany_berlin': 7,
                         'Europe_italy_Rome': 3,
                         'USA_washington': 1,
                         'USA_New York': 4}
nested = {'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}

flatten_dict(nested) => {'Q_w_E_r_T_y': 123}
not_nested = {'a': 100, 'b': 200}

flatten_dict(not_nested) => {'a': 100, 'b': 200}
Ваша задача только написать определение функции flatten_dict
"""


from typing import Dict, Union, Optional

NestedDict = Dict[str, Optional[Union[int, "NestedDict"]]]


def flatten_dict(dictionary: NestedDict) -> dict[str, int]:
    """Преобразовывает многоуровневый вложенный словарь в плоский"""
    result = {}
    for key, value in dictionary.items():
        if isinstance(value, dict):
            nested_result = flatten_dict(value)
            for nested_key, nested_value in nested_result.items():
                result[f"{key}_{nested_key}"] = nested_value
        else:
            result[key] = value

    return result


nested = {'Germany': {'berlin': 7},
          'Europe': {'italy': {'Rome': 3}},
          'USA': {'washington': 1, 'New York': 4}}
assert flatten_dict(nested) == {'Germany_berlin': 7,
                         'Europe_italy_Rome': 3,
                         'USA_washington': 1,
                         'USA_New York': 4}

nested = {'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}
assert flatten_dict(nested) == {'Q_w_E_r_T_y': 123}

not_nested = {'a': 100, 'b': 200}
assert flatten_dict(not_nested) == {'a': 100, 'b': 200}

nested1 = {'A': {'B': {'C': {'D': {'E': {'F': {'G': {'H': 9876}}}}}}}}
assert flatten_dict(nested1) == {'A_B_C_D_E_F_G_H': 9876}

nested2 = {'one': {'two': {'three': {'four': {'five': {'six': {'seven': {'eight': 8765}}}}}}}}
assert flatten_dict(nested2) == {'one_two_three_four_five_six_seven_eight': 8765}

nested3 = {'a': {'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': 5432}}}}}}}}}
assert flatten_dict(nested3) == {'a_b_c_d_e_f_g_h_i': 5432}

nested4 = {'X': {'Y': {'Z': {'W': {'V': {'U': {'T': {'S': {'R': 2109}}}}}}}}}
assert flatten_dict(nested4) == {'X_Y_Z_W_V_U_T_S_R': 2109}

nested5 = {'apple': {'orange': {'banana': {'grape': {'kiwi': {'mango': {'pear': {'peach': 9876}}}}}}}}
assert flatten_dict(nested5) == {'apple_orange_banana_grape_kiwi_mango_pear_peach': 9876}

nested6 = {'key1': {'key2': {'key3': {'key4': {'key5': {'key6': {'key7': {'key8': 8765}}}}}}}}
assert flatten_dict(nested6) == {'key1_key2_key3_key4_key5_key6_key7_key8': 8765}

nested7 = {'a': {'b': {'c': {'d': {'e': {'f': {'g': {'h': 5432}}}}}}}}
assert flatten_dict(nested7) == {'a_b_c_d_e_f_g_h': 5432}

nested8 = {'alpha': {'beta': {'gamma': {'delta': {'epsilon': {'zeta': {'eta': {'theta': 2109}}}}}}}}
assert flatten_dict(nested8) == {'alpha_beta_gamma_delta_epsilon_zeta_eta_theta': 2109}

nested9 = {'cat': {'dog': {'bird': {'fish': {'rabbit': {'turtle': {'hamster': {'parrot': 9876}}}}}}}}
assert flatten_dict(nested9) == {'cat_dog_bird_fish_rabbit_turtle_hamster_parrot': 9876}

nested10 = {'a': {'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': 5432}}}}}}}}}}
assert flatten_dict(nested10) == {'a_b_c_d_e_f_g_h_i_j': 5432}

print('Все проверки пройдены!')
