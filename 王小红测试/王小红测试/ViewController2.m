//
//  ViewController2.m
//  王小红测试
//
//  Created by GuangdongQi on 2018/8/16.
//  Copyright © 2018年 GuangdongQi. All rights reserved.
//

#import "ViewController2.h"
#import "SetingTableViewController.h"

@interface ViewController2 ()

@property (nonatomic, strong) UIButton *setingButton;

@end

@implementation ViewController2

- (UIButton *)setingButton
{
    if (_setingButton == nil){
        _setingButton = [UIButton new];
        _setingButton.titleLabel.font = [UIFont systemFontOfSize:14];
        [_setingButton setTitle:@"设置" forState:UIControlStateNormal];
        [_setingButton setTitleColor:[UIColor redColor] forState:UIControlStateNormal];
        [_setingButton addTarget:self action:@selector(setingButtonAction) forControlEvents:UIControlEventTouchUpInside];
    }
    return _setingButton;
}

- (void)viewDidLoad {
    [super viewDidLoad];
    self.navigationItem.rightBarButtonItem = [[UIBarButtonItem alloc]initWithCustomView:self.setingButton];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void)setingButtonAction
{
    [self.navigationController pushViewController:[SetingTableViewController new] animated:YES];
}

@end
