//
//  SetingTableViewController.m
//  王小红测试
//
//  Created by GuangdongQi on 2018/8/16.
//  Copyright © 2018年 GuangdongQi. All rights reserved.
//

#import "SetingTableViewController.h"
#import "AboutTableViewController.h"

@interface SetingTableViewController ()

@property (nonatomic, strong) UIButton *quitAccountButton;

@end

@implementation SetingTableViewController

- (UIButton *)quitAccountButton
{
    if (_quitAccountButton == nil){
        _quitAccountButton = [UIButton new];
        _quitAccountButton.backgroundColor = [UIColor redColor];
        [_quitAccountButton setTitle:@"退出账号" forState:UIControlStateNormal];
        [_quitAccountButton setTitleColor:[UIColor whiteColor] forState:UIControlStateNormal];
        _quitAccountButton.layer.masksToBounds = YES;
        _quitAccountButton.layer.cornerRadius = 3;
    }
    return _quitAccountButton;
}

- (void)viewDidLoad {
    [super viewDidLoad];
    
    self.navigationItem.title = @"设置";
    
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

#pragma mark - Table view data source

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {

    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {

    return 2;
}


- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"cell"];
    if (!cell) {
        
        cell = [[UITableViewCell alloc]initWithStyle:UITableViewCellStyleValue1 reuseIdentifier:@"cell"];
    }
    
    cell.preservesSuperviewLayoutMargins = NO;
    cell.separatorInset = UIEdgeInsetsZero;
    cell.layoutMargins = UIEdgeInsetsZero;
    
    if (indexPath.row == 0) {
        cell.textLabel.text = @"清理缓存";
        cell.detailTextLabel.text = @"9.1m";
        cell.detailTextLabel.font = [UIFont systemFontOfSize:14];
    }else{
        cell.textLabel.text = @"关于";
        cell.accessoryType = UITableViewCellAccessoryDisclosureIndicator;
    }
    
    return cell;
}

- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath
{
    return 50;
}

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    [tableView deselectRowAtIndexPath:indexPath animated:YES];
    
    if (indexPath.row == 0) {
        [self showAlertController];
    }else{
        [self.navigationController pushViewController:[AboutTableViewController new] animated:YES];
    }
}

- (CGFloat)tableView:(UITableView *)tableView heightForHeaderInSection:(NSInteger)section {
    
    return 1.f;
}

- (CGFloat)tableView:(UITableView *)tableView heightForFooterInSection:(NSInteger)section {
    
    return self.view.frame.size.width;
}

- (UIView *)tableView:(UITableView *)tableView viewForHeaderInSection:(NSInteger)section {
    
    UIView *view = [UIView new];
    view.backgroundColor = [UIColor clearColor];
    
    return view;
}

- (UIView *)tableView:(UITableView *)tableView viewForFooterInSection:(NSInteger)section {
    
    UIView *view = [UIView new];
    view.backgroundColor = [UIColor clearColor];
    
    UIView *lineView = [UIView new];
    lineView.backgroundColor = UIColorFromRGB(0xe5e5e5);
    lineView.frame = CGRectMake(0, 0, self.view.frame.size.width, 1);
    [view addSubview:lineView];
    
    self.quitAccountButton.frame = CGRectMake(25, 60, self.view.frame.size.width - 50, 50);
    [view addSubview:self.quitAccountButton];
    
    return view;
    
}

- (void)showAlertController{
    UIAlertController *alertController = [UIAlertController alertControllerWithTitle:@"" message:@"确认清除全部缓存" preferredStyle:UIAlertControllerStyleAlert];
    UIAlertAction *cancelAction = [UIAlertAction actionWithTitle:@"取消" style:UIAlertActionStyleCancel handler:nil];
    
    UIAlertAction *setAction = [UIAlertAction actionWithTitle:@"确定" style:UIAlertActionStyleDefault handler:^(UIAlertAction * _Nonnull action) {
        
        
    }];
    
    [alertController addAction:cancelAction];
    [alertController addAction:setAction];
    [self presentViewController:alertController animated:YES completion:nil];
}
@end
