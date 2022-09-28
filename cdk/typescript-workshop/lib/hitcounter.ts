import { Construct } from 'constructs';
import { Function, IFunction, Runtime, Code } from 'aws-cdk-lib/aws-lambda';
import { Table, AttributeType, TableEncryption } from 'aws-cdk-lib/aws-dynamodb';
import { RemovalPolicy } from 'aws-cdk-lib';

export interface HitCounterProps {
    /** the function for which we want to count url hits **/
    downstream: IFunction;
}

export class HitCounter extends Construct {

    /** allows accessing the counter function */
    public readonly handler: Function;

    /** the hit counter table */
    public readonly table: Table;

    constructor(scope: Construct, id: string, props: HitCounterProps) {
        super(scope, id);

        const table = new Table(this, 'Hits', {
            partitionKey: { name: 'path', type: AttributeType.STRING },
            removalPolicy: RemovalPolicy.DESTROY,
            encryption: TableEncryption.AWS_MANAGED,
        });
        this.table = table;

        this.handler = new Function(this, 'HitCounterHandler', {
            runtime: Runtime.NODEJS_14_X,
            code: Code.fromAsset('lambda'),
            handler: 'hitcounter.handler',
            environment: {
                DOWNSTREAM_FUNCTION_NAME: props.downstream.functionName,
                HITS_TABLE_NAME: table.tableName,
            },
        });

        // grant the lambda role read/write permissions to our table
        table.grantReadWriteData(this.handler);

        // grant the lambda role invoke permissions to the downstream function
        props.downstream.grantInvoke(this.handler);
    }
}