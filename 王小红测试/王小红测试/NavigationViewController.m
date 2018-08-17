//
//  NavigationViewController.m
//  王小红测试
//
//  Created by GuangdongQi on 2018/8/16.
//  Copyright © 2018年 GuangdongQi. All rights reserved.
//

#import "NavigationViewController.h"

@interface NavigationViewController ()

@property (nonatomic, strong) UIButton *backButton;

@end

@implementation NavigationViewController

- (UIButton *)backButton
{
    if (_backButton == nil){
        _backButton = [UIButton new];
        [_backButton setTitle:@"返回" forState:UIControlStateNormal];
        [_backButton setTitleColor:[UIColor whiteColor] forState:UIControlStateNormal];
        _backButton.titleLabel.font = [UIFont systemFontOfSize:15];
        [_backButton addTarget:self action:@selector(backAction) forControlEvents:UIControlEventTouchUpInside];
    }
    return _backButton;
}

- (void)viewDidLoad {
    [super viewDidLoad];
    
    if (self.navigationController.viewControllers.count > 1) {
        self.navigationItem.leftBarButtonItem = [[UIBarButtonItem alloc]initWithCustomView:self.backButton];
    }
    self.edgesForExtendedLayout = UIRectEdgeNone;

}

- (void)backAction
{
    if (self.navigationController.viewControllers.count > 1) {
        [self.navigationController popViewControllerAnimated:YES];
    }else{
        [self dismissViewControllerAnimated:YES completion:nil];
    }
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}



@end
