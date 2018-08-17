//
//  EditionViewController.m
//  王小红测试
//
//  Created by GuangdongQi on 2018/8/16.
//  Copyright © 2018年 GuangdongQi. All rights reserved.
//

#import "EditionViewController.h"

@interface EditionViewController ()

@end

@implementation EditionViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    self.conterLabel.text = @"2018年08月10日\n1、为用户增加党员身份标识。\n2、修复了其他已知问题";
    
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
