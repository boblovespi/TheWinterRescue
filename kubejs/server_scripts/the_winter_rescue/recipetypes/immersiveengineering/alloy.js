onEvent('recipes', (event) => {
    let recipes = [
            {
                input1: 'minecraft:cobblestone',
                input2: 'minecraft:cobblestone',
                output: Item.of('minecraft:stone', 2),
                time: 200
            },
            {input1: '#forge:stone', input2: '#forge:stone', output: Item.of('minecraft:stone', 2), time: 200},
            {input1: '8x minecraft:sand', input2: 'kubejs:charcoal_dust', output: '8x minecraft:glass', time: 800},
            {
                input1: '3x #forge:ingots/lead',
                input2: '#forge:ingots/antimony',
                output: '4x kubejs:battery_alloy',
                time: 400
            },
			{input1: '#forge:ingots/zinc', input2: '2x #forge:ingots/copper', output: '3x rankine:brass_ingot', time: 300},
            // {
            //     input1: '#forge:glass',
            //     input2: Ingredient.of('#forge:ingots/copper', 3),
            //     output: Item.of('tconstruct:tinkers_bronze_ingot', 3)
            // }
            {input1: '4x #forge:ores/copper', input2: '#kubejs:kiln_dust', output: '4x rankine:copper_ingot', time: 400},
            {input1: '4x #forge:ores/tin', input2: '#kubejs:kiln_dust', output: '4x rankine:tin_ingot', time: 400},
            {input1: 'charcoal_pit:unfired_brick', input2: 'charcoal_pit:unfired_brick', output: Item.of('minecraft:brick', 2), time:200}, 
            {input1: 'minecraft:clay', input2: 'minecraft:clay', output: Item.of('minecraft:terracotta', 2), time:200},
            {input1: 'rankine:fire_clay_ball', input2: 'rankine:fire_clay_ball', output: Item.of('rankine:refractory_brick', 2), time:200},
            {input1: 'charcoal_pit:unfired_sandy_brick', input2: 'charcoal_pit:unfired_sandy_brick', output: Item.of('charcoal_pit:sandy_brick_item', 2), time:200}
        ]
    recipes.forEach((recipe) => {
        event.recipes.immersiveengineering.alloy(recipe.output, recipe.input1, recipe.input2, recipe.time);
        // if (recipe.id) {
        //     re.id(recipe.id);
        // }
    });
});
