/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */
export function cookingStatus(minutes) {
  if (minutes == 0){
    return 'Lasagna is done.'
  }else if (minutes > 0){
    return 'Not done, please wait.'
  }else{
    return 'You forgot to set the timer.'
  }
}

export function preparationTime(layers = 0, prepTime = 2) {
  return layers.length * prepTime
}

export function quantities(layers) {
  const obj = {sauce: 0, noodles: 0}
  for (let layer of layers) {
    if (layer == 'sauce'){
      obj[layer] += 0.2
    }else if (layer == 'noodles'){
      obj[layer] += 50
    }else{
      continue
    }
  }
  console.log(obj)
  return obj
}

export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList[friendsList.length - 1])
}

export function scaleRecipe(recipe, amount) {
  const scaled = {};
  for (const key in recipe) {
    scaled[key] = recipe[key] * amount / 2;
  }
  return scaled;
}