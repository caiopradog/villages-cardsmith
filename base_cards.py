from card import TYPE, COLOR, EXPANSION

base_cards = [{
    "name": "Mosqueteiro",
    "ability": '+3 força contra unidades da mesma cor.',
    "type": TYPE.UNIT,
    "power": 2,
    "gold": 1,
    "unit": 'ace',
    "colors": [COLOR.YELLOW, COLOR.PURPLE],
    "alt_colors": [COLOR.GREEN, COLOR.BLUE],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Arqueira",
    "ability": 'Pode defender qualquer uma de suas vilas. '
               '+3 força ao defender uma vila onde esta unidade não reside.',
    "type": TYPE.UNIT,
    "power": 2,
    "gold": 2,
    "unit": 'archer',
    "colors": [COLOR.ORANGE],
    "alt_colors": [COLOR.GREEN],
    "gender": "f",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Assassino",
    "ability": 'Sempre vence quando contratado para atacar.',
    "type": TYPE.UNIT,
    "power": 1,
    "gold": 3,
    "unit": 'assassin',
    "colors": [COLOR.PURPLE],
    "alt_colors": [COLOR.RED],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Construtor",
    "ability": 'Permite construções na vila onde esta unidade reside.',
    "type": TYPE.UNIT,
    "power": 1,
    "gold": 3,
    "unit": 'builder',
    "colors": [COLOR.PURPLE, COLOR.BLUE, COLOR.ORANGE],
    "alt_colors": [COLOR.RED, COLOR.YELLOW, COLOR.GREEN],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Dragão",
    "ability": '',
    "type": TYPE.UNIT,
    "power": 5,
    "gold": 2,
    "unit": 'dragon',
    "colors": [COLOR.RED],
    "alt_colors": [COLOR.ORANGE],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Fazendeiro",
    "ability": 'Permite animais na vila onde esta unidade reside.',
    "type": TYPE.UNIT,
    "power": 1,
    "gold": 3,
    "unit": 'farmer',
    "colors": [COLOR.RED, COLOR.YELLOW, COLOR.GREEN],
    "alt_colors": [COLOR.PURPLE, COLOR.BLUE, COLOR.ORANGE],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Goblin",
    "ability": '+2 força contra o jogador com a carta "Pontuação Alta".',
    "type": TYPE.UNIT,
    "power": 2,
    "gold": 1,
    "unit": 'goblin',
    "colors": [COLOR.BLUE, COLOR.YELLOW],
    "alt_colors": [COLOR.RED],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Golem",
    "ability": '+2 força ao defender uma vila. +1 força para cada construção na vila onde esta unidade reside.',
    "type": TYPE.UNIT,
    "power": 2,
    "gold": 2,
    "unit": 'golem',
    "colors": [COLOR.GREEN],
    "alt_colors": [COLOR.YELLOW],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Herói",
    "ability": '+2 força quando usado pelo jogador com a carta "Pontuação Baixa".',
    "type": TYPE.UNIT,
    "power": 3,
    "gold": 2,
    "unit": 'hero',
    "colors": [COLOR.BLUE],
    "alt_colors": [COLOR.GREEN],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Coringa",
    "ability": 'Quando usado na batalha, a unidade com menos força vence, e no empate o defensor vence.',
    "type": TYPE.UNIT,
    "power": 2,
    "gold": 1,
    "unit": 'joker',
    "colors": [COLOR.GREEN],
    "alt_colors": [COLOR.PURPLE],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Rei",
    "ability": 'Dobra o valor total da vila onde esta unidade reside. '
               'Não possui efeito na mão ou no cemitério.',
    "type": TYPE.UNIT,
    "power": 0,
    "gold": 0,
    "unit": 'king',
    "colors": [COLOR.GREEN],
    "alt_colors": [COLOR.YELLOW],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Cavaleiro",
    "ability": '+1 força ao defender uma vila. '
               '+3 força contra dragões.',
    "type": TYPE.UNIT,
    "power": 2,
    "gold": 1,
    "unit": 'knight',
    "colors": [COLOR.YELLOW, COLOR.GREEN],
    "alt_colors": [COLOR.BLUE, COLOR.PURPLE],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Comerciante",
    "ability": 'Como sua fase de agir, você e outro jogador podem trocar uma carta de suas mãos. '
               'O outro jogador não pode recusar essa ação.',
    "type": TYPE.UNIT,
    "power": 0,
    "gold": 3,
    "unit": 'merchant',
    "colors": [COLOR.ORANGE],
    "alt_colors": [COLOR.YELLOW],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Orc",
    "ability": 'Ao atacar, a força desta unidade é igual ao número de unidades na vila atacada.',
    "type": TYPE.UNIT,
    "power": 2,
    "gold": 2,
    "unit": 'orc',
    "colors": [COLOR.RED],
    "alt_colors": [COLOR.ORANGE],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Padre",
    "ability": 'Seu valor de ouro é igual ao número de cartas no cemitério.',
    "type": TYPE.UNIT,
    "power": 0,
    "gold": 0,
    "unit": 'priest',
    "colors": [COLOR.ORANGE],
    "alt_colors": [COLOR.RED],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Princesa",
    "ability": '',
    "type": TYPE.UNIT,
    "power": 0,
    "gold": 5,
    "unit": 'princess',
    "colors": [COLOR.GREEN, COLOR.BLUE],
    "alt_colors": [COLOR.YELLOW, COLOR.PURPLE],
    "gender": "f",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Batedora",
    "ability": 'Depois da batalha, seu oponente deve mostrar sua mão e descartar uma carta aleatória, '
               'mesmo se você perdeu.',
    "type": TYPE.UNIT,
    "power": 1,
    "gold": 1,
    "unit": 'scout',
    "colors": [COLOR.RED, COLOR.PURPLE],
    "alt_colors": [COLOR.ORANGE],
    "gender": "f",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Ladra",
    "ability": 'Depois da batalha, você pode roubar uma carta da mão do seu oponente, mesmo se você perdeu.',
    "type": TYPE.UNIT,
    "power": 1,
    "gold": 1,
    "unit": 'thief',
    "colors": [COLOR.YELLOW],
    "alt_colors": [COLOR.BLUE, COLOR.PURPLE],
    "gender": "f",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Guerreiro",
    "ability": '+1 força ao atacar. Como sua recompensa de batalha, você pode destruir uma construção da vila atacada.',
    "type": TYPE.UNIT,
    "power": 2,
    "gold": 1,
    "unit": 'warrior',
    "colors": [COLOR.ORANGE, COLOR.BLUE],
    "alt_colors": [COLOR.RED],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Mago",
    "ability": '-3 força contra unidades da mesma cor.',
    "type": TYPE.UNIT,
    "power": 4,
    "gold": 2,
    "unit": 'wizard',
    "colors": [COLOR.RED, COLOR.PURPLE],
    "alt_colors": [COLOR.ORANGE, COLOR.BLUE],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Coelho",
    "ability": 'Destrua a qualquer momento para cancelar a próxima fase de agir de qualquer jogador.',
    "type": TYPE.ANIMAL,
    "power": 0,
    "gold": 1,
    "unit": 'bunny',
    "colors": [COLOR.LIGHT],
    "alt_colors": [COLOR.GRAY],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Galinha",
    "ability": 'Destrua a qualquer momento para comprar 2 cartas.',
    "type": TYPE.ANIMAL,
    "power": 0,
    "gold": 1,
    "unit": 'chicken',
    "colors": [COLOR.LIGHT],
    "alt_colors": [COLOR.GRAY],
    "gender": "f",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Porco",
    "ability": 'Destrua ao enviar uma unidade da vila onde este animal reside para batalha. '
               '+2 força à unidade.',
    "type": TYPE.ANIMAL,
    "power": 0,
    "gold": 1,
    "unit": 'pig',
    "colors": [COLOR.LIGHT],
    "alt_colors": [COLOR.GRAY],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Ovelha",
    "ability": 'Destrua quando uma unidade da vila onde este animal reside perde uma batalha. '
               'A unidade volta à vila e não pode ser destruída ou sequestrada.',
    "type": TYPE.ANIMAL,
    "power": 0,
    "gold": 1,
    "unit": 'sheep',
    "colors": [COLOR.GRAY],
    "alt_colors": [],
    "gender": "f",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Castelo",
    "ability": '+1 força às unidades defensoras que residem na vila que possui esta construção.',
    "type": TYPE.BUILDING,
    "power": 0,
    "gold": 4,
    "unit": 'castle',
    "colors": [COLOR.GRAY],
    "alt_colors": [],
    "gender": "m",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Pousada",
    "ability": 'Permite que uma unidade de cor diferente resida na vila que possui esta construção. '
               'A unidade pode retornar à sua mão no seu próximo turno.',
    "type": TYPE.BUILDING,
    "power": 0,
    "gold": 3,
    "unit": 'inn',
    "colors": [COLOR.LIGHT],
    "alt_colors": [COLOR.GRAY],
    "gender": "f",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Taverna",
    "ability": 'Como sua fase de compra, você pode comprar uma carta qualquer da pilha de descarte.',
    "type": TYPE.BUILDING,
    "power": 0,
    "gold": 3,
    "unit": 'tavern',
    "colors": [COLOR.GRAY],
    "alt_colors": [],
    "gender": "f",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Torre",
    "ability": 'Revele unidades contratadas que atacam a vila que possui esta construção '
               'antes de escolher unidades defensoras',
    "type": TYPE.BUILDING,
    "power": 0,
    "gold": 3,
    "unit": 'tower',
    "colors": [COLOR.GRAY],
    "alt_colors": [],
    "gender": "f",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Pontuação Alta",
    "ability": 'Ao fim de cada rodada, o jogador com maior pontuação receberá esta carta. No caso de empate, ninguém recebe esta carta. \n \n A abilidade de algumas cartas se referem à esta carta e seu dono.',
    "type": TYPE.SCORE,
    "power": 0,
    "gold": 0,
    "unit": 'highscore',
    "colors": [COLOR.GRAY],
    "alt_colors": [],
    "gender": "f",
    "exp_icon": EXPANSION.BASE
  }, {
    "name": "Pontuação Baixa",
    "ability": 'Ao fim de cada rodada, o jogador com menor pontuação receberá esta carta. No caso de empate, ninguém recebe esta carta. \n \n A abilidade de algumas cartas se referem à esta carta e seu dono.',
    "type": TYPE.SCORE,
    "power": 0,
    "gold": 0,
    "unit": 'lowscore',
    "colors": [COLOR.GRAY],
    "alt_colors": [],
    "gender": "f",
    "exp_icon": EXPANSION.BASE
  }]
