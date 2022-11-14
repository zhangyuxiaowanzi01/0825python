-- A. 查询卖的最贵的商品的名称
# 1. 查询最高价格 
SELECT MAX(shop_price) FROM ecs_goods;
# 2. 通过最高价格获取对应商品名称
SELECT goods_name, shop_price FROM ecs_goods WHERE shop_price = 
(SELECT MAX(shop_price) FROM ecs_goods);

   
-- B. 查询商品品牌为”仓品”的 所有商品名称和商品价格
# 1. 通过品牌名称查询对应品牌id
# 2. 通过品牌id查询商品价格名称
SELECT goods_name, shop_price FROM ecs_goods WHERE brand_id = 
(SELECT brand_id FROM ecs_brand WHERE brand_name='仓品');


-- C. 查询商品品牌为”仓品”的 所有商品名称和商品价格 按照价格降序排列
SELECT goods_name, shop_price FROM ecs_goods WHERE brand_id = 
(SELECT brand_id FROM ecs_brand WHERE brand_name='仓品')
ORDER BY shop_price DESC;

-- D. 查询每个商品品牌的商品数量
-- SELECT brand_id, SUM(goods_number) FROM ecs_goods GROUP BY brand_id;
SELECT brand_id, count(*) FROM ecs_goods GROUP BY brand_id;
# goods g brand b
# 第一种
SELECT b.brand_name, b.brand_id, count(g.goods_id) FROM 
ecs_brand b INNER JOIN ecs_goods g
on b.brand_id = g.brand_id GROUP BY g.brand_id;
# 第二种
SELECT b.brand_name, b.brand_id, count(g.goods_id) FROM
ecs_brand b, ecs_goods g
WHERE b.brand_id = g.brand_id GROUP BY g.brand_id;

-- E. 查询商品品牌对应的商品数量大于5的商品品牌名称
SELECT b.brand_name, b.brand_id, count(g.goods_id) FROM
ecs_brand b, ecs_goods g
WHERE b.brand_id = g.brand_id GROUP BY g.brand_id HAVING COUNT(*) > 5;


