//
//  TabbarViewController.m
//  王小红测试
//
//  Created by GuangdongQi on 2018/8/16.
//  Copyright © 2018年 GuangdongQi. All rights reserved.
//

#import "TabbarViewController.h"
#import "NavigationViewController.h"
#import "ViewController1.h"
#import "ViewController2.h"

@interface TabbarViewController ()

@end

@implementation TabbarViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    ViewController1 *controller1 = [ViewController1 new];
    controller1.title = @"首页";
    ViewController2 *controller2 = [ViewController2 new];
    controller2.title = @"我的";
    
    NSArray *controllers = @[controller1,controller2];
    
    NSMutableArray *navs = [NSMutableArray new];
    
    for (UIViewController *vc in controllers) {
        
        NavigationViewController  *navigation = [[NavigationViewController alloc] initWithRootViewController:vc];
        
        [navs addObject:navigation];
    }
    
    [self setViewControllers:navs];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
